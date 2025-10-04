"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    # Leer el archivo desde la ruta del proyecto
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    
    # Limpiar nombres y valores por si hay espacios
    df.columns = df.columns.str.strip()
    df["c4"] = df["c4"].astype(str).str.strip()
    
    # Agrupar por c0, ordenar alfabéticamente los valores de c4 y unir con ','
    resultado = (
        df.groupby("c0", as_index=False)
          .agg({"c4": lambda x: ",".join(sorted(x.tolist()))})
    )
    
    # Asegurar orden por c0 y resetear índice para que coincida exactamente con la prueba
    resultado = resultado.sort_values("c0").reset_index(drop=True)
    
    return resultado