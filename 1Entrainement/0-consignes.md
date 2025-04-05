### 🛠️ Exercice 1 : Structuration d'une base de données avec Pandas

#### Objectif :
Créer une base de données structurée en utilisant Pandas, représentant des paramètres typiques d'un procédé de fabrication additive métallique.

#### Tâches :

- Créer un script Python générant aléatoirement des données représentant des paramètres comme :
  - Puissance laser (en watts)
  - Vitesse de déplacement (en mm/s)
  - Débit de poudre (en g/min)

- Enregistrer ces données dans un DataFrame Pandas bien organisé.
- Exporter le DataFrame vers un fichier CSV.
- Lire ce CSV dans un nouveau script et effectuer une analyse rapide (moyenne, écart type, min, max).

#### Bibliothèques à utiliser :
- Pandas
- NumPy

---

### 📈 Exercice 2 : Application de modèles de classification simple avec Scikit-learn

#### Objectif :
Simuler un problème de classification binaire pour identifier des anomalies dans les paramètres.

#### Tâches :

- À partir du DataFrame précédent, ajoute une colonne représentant des anomalies fictives (0 ou 1).
- Sépare tes données en ensembles d'entraînement et de test avec `train_test_split`.
- Entraîne un modèle de classification (exemple : RandomForestClassifier) pour prédire les anomalies.
- Évalue les performances du modèle à l'aide des métriques suivantes :
  - Précision
  - Rappel
  - F1-score

#### Bibliothèques à utiliser :
- Scikit-learn
- Pandas

---

### 🧠 Exercice 3 : Classification avec réseaux de neurones (нейронные сети [neyronnye seti] réseaux neuronaux)

#### Objectif :
Construire et entraîner un modèle simple de réseau de neurones avec PyTorch ou TensorFlow pour classifier les anomalies.

#### Tâches :

- Normalise les données de l'exercice précédent.
- Crée un réseau neuronal avec les couches suivantes :
  - Une couche d'entrée correspondant aux paramètres de ton DataFrame.
  - Deux couches cachées avec activation ReLU.
  - Une couche de sortie avec une activation sigmoid pour la classification binaire.

- Entraîne le modèle avec une fonction de perte adaptée (exemple : BCE Loss pour PyTorch ou BinaryCrossentropy pour TensorFlow).
- Trace les courbes de perte et d'exactitude sur les ensembles d'entraînement et de validation.

#### Bibliothèques à utiliser :
- PyTorch ou TensorFlow
- Matplotlib pour la visualisation des performances

---

### 🧹 Exercice bonus : Développement d'une interface simple (интерфейс [interface] interface) en C++

#### Objectif :
Simuler l'affichage et la gestion des paramètres d'un procédé via un programme en C++.

#### Tâches :

- Créer une structure de données (`struct`) représentant les paramètres de procédé (laser, vitesse, débit).
- Implémente une interface en ligne de commande qui permet de :
  - Ajouter un paramètre.
  - Modifier un paramètre.
  - Afficher tous les paramètres actuels.