def my_analysis():
    print("""
    # Mostrar el tamaño (dimensión) del dataset: número de filas y columnas
    print("Tamaño del dataset:")
    print(f"Número de filas: {df.shape[0]}")
    print(f"Número de columnas: {df.shape[1]}\n")

    # Mostrar los nombres de todas las columnas presentes en el dataset
    print("Columnas del dataset:")
    print(df.columns)
    print()

    #############################################################################3

    # Comprobar si hay valores nulos en cada columna y contar cuántos son
    print("Número de valores nulos por columna:")
    print(df.isnull().sum())
    print()

    # Eliminamos la columna llamada 'None'
    # Esta columna contiene valores irrelevantes ("NONE") que no aportan ningún valor
    # Al eliminarla, mejoramos la eficiencia del modelo y reducimos la
    # dimensionalidad del dataset.
    df = df.drop(columns=[None])

    # Verificamos que la columna 'None' ha sido eliminada correctamente
    # Al imprimir nuevamente los nombres de las columnas, podemos asegurarnos de que la columna ha sido eliminada.
    print("\nNombres de las columnas después de la eliminación:", df.columns)

    ##################################################################################3

    # Verificar si existen columnas completamente vacías (todas sus celdas nulas)
    empty_cols = df.columns[df.isnull().all()]
    if len(empty_cols) > 0:
        print("Columnas completamente vacías (todas sus celdas son nulas):")
        print(list(empty_cols))
    else:
        print("No hay columnas completamente vacías.")
    print()

    # Mostrar el tipo de datos (dtype) de cada columna, para saber si son numéricas, de texto, etc.
    print("Tipos de datos de las columnas:")
    print(df.dtypes)
    print()

    # Mostrar un resumen estadístico básico de todas las columnas numéricas
    print("Resumen estadístico de las variables numéricas:")
    print(df.describe().transpose())
    # Esta medida muestras valores atipicos, algo que veremos con mas tranquilidad
    # en la parte de lso outliners

    # Análisis detallado de las características numéricas
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    print("Características numéricas analizadas:", list(numeric_cols))
    print()

    for col in numeric_cols:
        print(f"Analizando la variable numérica: {col}")
        print(f"Media: {df[col].mean():.2f}")
        print(f"Desviación estándar: {df[col].std():.2f}")
        print(f"Mínimo: {df[col].min()}")
        print(f"Máximo: {df[col].max()}")
        print()

    # Análisis detallado de las características categóricas
    categorical_cols = df.select_dtypes(include=['object']).columns
    print("Características categóricas analizadas:", list(categorical_cols))
    print()

    for col in categorical_cols:
        print(f"Analizando la variable categórica: {col}")
        print(f"Número de categorías: {df[col].nunique()}")
        print(f"Moda (categoría más frecuente): {df[col].mode()[0]}")
        print()"

    """)