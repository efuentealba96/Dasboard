# importamos la libreria con la que vamos a trabajar
import pandas as pd 

# indicamos la dirección de la cual se obtendran los datos
# necesarios para el dashboard
csv_file = pd.DataFrame(pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/input/RegistroCivil/Nacimientos/Nacimientos_2019-01-01_2019-12-31_DO.csv", sep = ",", header = 0, index_col = False)) 
# indicamos el formato de carga de los archivos
csv_file.to_json("Nacimientos.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None) 

