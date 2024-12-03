import pandas as pd
from io import StringIO

from data import data

def load_data():
    """
    Charge les données à partir du fichier CSV contenu dans la variable 'data'.
    """
    df = pd.read_csv(StringIO(data), sep=";")
    df['consumption_twh'] = df['consumption_twh'].str.replace(',', '.').astype(float)
    return df

def find_max_consumption(df):
    """
    Trouve la ligne avec la consommation maximale dans le DataFrame.
    """
    max_row = df.loc[df['consumption_twh'].idxmax()]
    return max_row

def print_max_consumption():
    """
    Affiche le résultat de la consommation maximale.
    """
    df = load_data()
    max_row = find_max_consumption(df)
    print(f"Région: {max_row['Region']}")
    print(f"Date: {max_row['Date']}")
    print(f"Consommation maximale: {max_row['consumption_twh']} TWh")

if __name__ == "__main__":
    print_max_consumption()

# Dans le fichier data.py, vous avez toutes les informations contenues dans le .csv.
# Les deux fichiers sont reliés pour que le résultat apparaisse sur functions.py.

# Voici le résultat final:
# Région: Île-de-France
# Date: 2016
# Consommation maximale: 74.0 TWh