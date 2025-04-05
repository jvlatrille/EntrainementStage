import pandas as pd
import numpy as np

# Générer des données fictives
np.random.seed(0)
data = {
    'Puissance_Laser_W': np.random.uniform(100, 1000, 100),
    'Vitesse_Deplacement_mm_s': np.random.uniform(10, 50, 100),
    'Debit_Poudre_g_min': np.random.uniform(5, 20, 100)
}

# Création du DataFrame
df = pd.DataFrame(data)

# Export en CSV
df.to_csv('parametres_procede.csv', index=False)
print("Données exportées dans parametres_procede.csv")

df = pd.read_csv('1Entrainement/parametres_procede.csv')

# Affichage
print("Moyenne :\n", df.mean())
print("\nÉcart-type :\n", df.std())
print("\nMin :\n", df.min())
print("\nMax :\n", df.max())

