import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Chargement des données
df = pd.read_csv('1Entrainement/parametres_procede.csv')

# Générer des anomalies fictives
np.random.seed(1)
df['Anomalie'] = np.random.choice([0, 1], size=len(df))

# Séparation des données
X = df[['Puissance_Laser_W', 'Vitesse_Deplacement_mm_s', 'Debit_Poudre_g_min']]
y = df['Anomalie']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modèle de classification
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prédiction et évaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
