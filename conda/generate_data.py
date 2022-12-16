# Importer les librairies
import numpy as np
import pandas as pd
import pyLogs as l

# Crée une matrice 10*100 de valeurs aléatoires
array = np.random.randint(10, size=(10, 100))

# Crée un dataframe à partir de la matrice
df = pd.DataFrame(array)

# Enregistre le fichier au format csv
df.to_csv("save.csv")

# Logs
l.l("Generate Data Finished", "s")