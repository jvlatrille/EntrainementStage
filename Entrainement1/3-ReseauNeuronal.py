import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chargement et préparation des données
df = pd.read_csv('Entrainement1/parametres_procede.csv')
df['Anomalie'] = np.random.choice([0, 1], size=len(df))

X = df[['Puissance_Laser_W', 'Vitesse_Deplacement_mm_s', 'Debit_Poudre_g_min']].values
y = df['Anomalie'].values.reshape(-1, 1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Conversion en tensors
X_train_tensor = torch.FloatTensor(X_train)
y_train_tensor = torch.FloatTensor(y_train)
X_test_tensor = torch.FloatTensor(X_test)
y_test_tensor = torch.FloatTensor(y_test)

# Définition du réseau
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(3, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

net = Net()

# Optimiseur et fonction de perte
criterion = nn.BCELoss()
optimizer = optim.Adam(net.parameters(), lr=0.01)

# Entraînement
epochs = 100
train_losses, test_losses = [], []

for epoch in range(epochs):
    net.train()
    optimizer.zero_grad()
    output = net(X_train_tensor)
    loss = criterion(output, y_train_tensor)
    loss.backward()
    optimizer.step()

    # Enregistrement des pertes
    train_losses.append(loss.item())
    
    net.eval()
    test_loss = criterion(net(X_test_tensor), y_test_tensor)
    test_losses.append(test_loss.item())

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss Train : {loss.item():.4f}, Loss Test : {test_loss.item():.4f}")

# Affichage des résultats
plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
