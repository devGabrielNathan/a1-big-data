import pandas as pd
import matplotlib.pyplot as plt

def import_csv():
    print("Importando CSV")
    try: 
        csv = pd.read_csv("csv/dataset.csv")
        print("CSV Importado com sucesso.")
        return csv

    except Exception as e:
        print("Ocorreu um erro ao importar o csv.", e)

