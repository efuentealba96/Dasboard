import pandas as pd 


def CSVtoJSON(csv):
    csv_file = pd.DataFrame(pd.read_csv(csv, sep = ",", header = 0, index_col = False))
    csv_file.to_json("Nacimientos.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

csv = str(input("Ingresar enlace de csv: "))

CSVtoJSON(csv)