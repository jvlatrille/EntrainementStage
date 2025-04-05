import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv('4Entrainement/donnees_meteo.csv')
df['Date'] = pd.to_datetime(df['Unnamed: 0'])
df['Jour'] = df['Date'].dt.day
df['Mois'] = df['Date'].dt.month
df['Annee'] = df['Date'].dt.year

X = df[['Jour', 'Mois', 'Annee', 'Humidite_%', 'Pression_hPa']]
y = df['Temperature_C']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('R²:', r2_score(y_test, y_pred))
print('MSE:', mean_squared_error(y_test, y_pred))
