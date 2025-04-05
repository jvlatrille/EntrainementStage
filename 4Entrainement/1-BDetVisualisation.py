import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('2023-01-01', periods=730)

df = pd.DataFrame({
    'Temperature_C': np.random.uniform(-5, 35, size=730),
    'Humidite_%': np.random.uniform(20, 100, size=730),
    'Pression_hPa': np.random.uniform(980, 1030, size=730)
}, index=dates)

df.to_csv('4Entrainement/donnees_meteo.csv')

# Visualisation température moyenne mensuelle
df_mensuel = df.resample('M').mean()
df_mensuel['Temperature_C'].plot(kind='line', marker='o')
plt.xlabel('Mois')
plt.ylabel('Température moyenne (°C)')
plt.title('Évolution mensuelle des températures moyennes')
plt.grid()
plt.show()
