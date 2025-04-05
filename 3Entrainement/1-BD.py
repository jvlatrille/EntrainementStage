import pandas as pd
import numpy as np

dates = pd.date_range(start='2024-01-01', periods=366, freq='D')
data = {
    'Temp_min': np.random.uniform(-5, 15, 366),
    'Temp_max': np.random.uniform(16, 35, 366)
}
df = pd.DataFrame(data, index=dates)
df['Temp_moy'] = (df['Temp_min'] + df['Temp_max']) / 2

df.to_csv('3Entrainement/meteo.csv')

# Analyse trimestrielle
print(df.resample('Q').mean())
