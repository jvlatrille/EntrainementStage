import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-01-01', periods=365)
data = {
    'Electricite_kWh': np.random.uniform(1000, 5000, 365),
    'Gaz_m3': np.random.uniform(500, 2000, 365),
    'Eau_litres': np.random.uniform(10000, 30000, 365)
}

df = pd.DataFrame(data, index=dates)
df.to_csv('2Entrainement/consommation_energetique.csv')

# Analyse mensuelle
df_mensuel = df.resample('M').mean()
print(df_mensuel)
