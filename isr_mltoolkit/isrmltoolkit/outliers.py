import numpy as np
import pandas as pd
from scipy.stats import zscore
from scipy.spatial.distance import mahalanobis
from sklearn.ensemble import IsolationForest
import seaborn as sns
import matplotlib.pyplot as plt


def multi_method_outlier_detection(df, contamination=0.05, z_thresh=3, maha_thresh=3):
    """
    Detecta outliers en un DataFrame utilizando múltiples métodos: IQR, Z-score, Mahalanobis y Isolation Forest.
    
    Parámetros:
    - df: DataFrame con los datos originales.
    - contamination: proporción esperada de outliers para IsolationForest.
    - z_thresh: umbral para Z-score.
    - maha_thresh: umbral para distancia de Mahalanobis.

    Retorna:
    - df_outlier_flag: DataFrame con flags booleanos de outliers por cada método.
    - outlier_counts: Conteo de outliers detectados por cada método.
    """
    df_out = df.copy()
    cols = df_out.select_dtypes(include=np.number).columns

    # Método IQR
    def detect_iqr_outliers(df, cols):
        outlier_flags = pd.DataFrame(index=df.index)
        for col in cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            outlier_flags[col] = ((df[col] < lower) | (df[col] > upper)).astype(int)
        return outlier_flags.sum(axis=1) > 0

    iqr_outliers = detect_iqr_outliers(df_out, cols)

    # Z-score
    z_scores = np.abs(zscore(df_out[cols].dropna()))
    z_outliers = (z_scores > z_thresh).any(axis=1)

    # Mahalanobis
    try:
        cov = np.cov(df_out[cols].dropna().T)
        inv_covmat = np.linalg.inv(cov)
        mean = df_out[cols].mean()
        maha_dist = df_out[cols].apply(lambda row: mahalanobis(row, mean, inv_covmat), axis=1)
        maha_outliers = maha_dist > maha_thresh
    except np.linalg.LinAlgError:
        maha_outliers = pd.Series([False] * len(df_out), index=df_out.index)

    # Isolation Forest
    iso_forest = IsolationForest(contamination=contamination, random_state=42)
    iso_outliers = iso_forest.fit_predict(df_out[cols])
    iso_outliers = iso_outliers == -1

    # DataFrame de resultados
    df_outlier_flag = pd.DataFrame({
        "IQR": iqr_outliers,
        "Z-score": z_outliers,
        "Mahalanobis": maha_outliers,
        "IsolationForest": iso_outliers
    })

    outlier_counts = df_outlier_flag.sum().sort_values(ascending=False)

    return df_outlier_flag, outlier_counts

def compare_boxplots(before_df, after_df, columns):
    """
    Muestra comparaciones de boxplots antes y después de la winsorización.

    Parámetros:
    - before_df: DataFrame original (antes de winsorización)
    - after_df: DataFrame modificado (después de winsorización)
    - columns: Lista de columnas a comparar
    """
    sns.set(style="whitegrid")
    plt.rcParams["figure.figsize"] = (12, 5)

    for col in columns:
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        sns.boxplot(data=before_df[col], ax=axes[0], color="salmon")
        axes[0].set_title(f"{col} - Before Winsorization", fontsize=12)
        axes[0].set_xlabel("")

        sns.boxplot(data=after_df[col], ax=axes[1], color="lightgreen")
        axes[1].set_title(f"{col} - After Winsorization", fontsize=12)
        axes[1].set_xlabel("")

        plt.suptitle(f"Boxplot Comparison: {col}", fontsize=14)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()
