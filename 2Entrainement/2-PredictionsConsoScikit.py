import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv('2Entrainement/consommation_energetique.csv')

X = df[['Gaz_m3', 'Eau_litres']]
y = df['Electricite_kWh']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print('MSE :', mean_squared_error(y_test, y_pred))
print('MAE :', mean_absolute_error(y_test, y_pred))
print('R² :', r2_score(y_test, y_pred))
