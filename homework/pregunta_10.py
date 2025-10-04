"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    # Leer el archivo (ruta según tu estructura)
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # Asegurarnos de no tener espacios raros en los nombres de columna
    df.columns = df.columns.str.strip()

    # Agrupar por c1, ordenar numéricamente los valores de cada grupo y unirlos con ':'
    s = df.groupby("c1")["c2"].apply(lambda x: ":".join(str(v) for v in sorted(x)))

    # Convertir a DataFrame, ordenar índices alfabéticamente y renombrar índice/columna según espera el test
    resultado = s.to_frame()
    resultado = resultado.sort_index()         # garantiza A, B, C, D, E
    resultado.index.name = "_c1"               # nombre del índice que espera el test
    resultado.columns = ["c2"]                 # nombre de la columna

    return resultado