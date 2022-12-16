# Importer les librairies
import pandas as pd
import pyLogs as l

# Compute function
def compute(x):
    return ( (x*x + 0.9) / 3) * 1500

# Ouvrir le fichier    
df = pd.read_csv("save.csv")

# Appliquer la fonction de calcul au fichier
df = df.apply(lambda x: compute(x))

# Sauvegarder le nouveau fichier
df.to_csv("results.csv")

# Logs
l.l("Compute Finished", "s")