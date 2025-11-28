"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel




def pregunta_01():
    import pandas as pd
    import re
    rows = []
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = lines[4:]

    current_cluster = None
    current_count = None
    current_percentage = None
    keywords_buffer = []

    for line in lines:
        if line.strip() == "":
            continue

        if re.match(r"^\s*\d+\s", line):

            if current_cluster is not None:
                keywords = " ".join(keywords_buffer)
                keywords = keywords.replace("%", "").strip()
                if keywords.endswith("."):
                    keywords = keywords[:-1]

                keywords = " ".join(keywords.split())

                rows.append([
                    current_cluster,
                    current_count,
                    current_percentage,
                    keywords,
                ])
            parts = re.split(r"\s{2,}", line.strip(), maxsplit=3)

            current_cluster = int(parts[0])
            current_count = int(parts[1])
            current_percentage = float(
                parts[2].replace("%", "").replace(",", ".").strip()
            )
            keywords_buffer = [parts[3].strip()]

        else:
            keywords_buffer.append(line.strip())
    if current_cluster is not None:
        keywords = " ".join(keywords_buffer)
        keywords = keywords.replace("%", "").strip()
        if keywords.endswith("."):
            keywords = keywords[:-1]
        keywords = " ".join(keywords.split())

        rows.append([
            current_cluster,
            current_count,
            current_percentage,
            keywords,
        ])
    df = pd.DataFrame(rows, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave",
    ])

    return df







    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    
    """
print(pregunta_01())


