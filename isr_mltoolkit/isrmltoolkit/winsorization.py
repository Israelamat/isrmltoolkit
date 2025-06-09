from scipy.stats.mstats import winsorize

def apply_winsorization(df, columnas, limits=(0.01, 0.01)):
    df_wins = df.copy()
    for col in columnas:
        data_col = df_wins[col].values
        df_wins[col] = winsorize(data_col, limits=limits)
    return df_wins
