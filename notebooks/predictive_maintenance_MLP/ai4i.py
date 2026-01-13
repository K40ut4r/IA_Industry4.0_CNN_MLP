import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Chargement du dataset
df = pd.read_csv('ai4i2020.csv')

# Nettoyage
df = df.drop(columns=['UDI', 'Product ID'])

# Encodage de la variable catégorielle 
df = pd.get_dummies(df, columns=['Type'], drop_first= True)

# Séparation des x et y 
X = df.drop(columns=['Machine failure']) # x=[type, Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min]]
y = df['Machine failure'] # y = [Machine failure]

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled,  #
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=42
                                                    )

# Création du modèle MLPClassifier
model = MLPClassifier(
    hidden_layer_sizes=(32, 16), # 2 couches cachées avec 32 et 16 neurones
    activation='relu', # fonction d'activation ReLU
    max_iter=500, # nombre maximal d'itérations
    random_state=42 # pour la reproductibilité
)

# Entrainement du modèle
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Acuracy :", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Température non normalisée
temp = X["Air temperature [K]"].values

plt.figure(figsize=(6, 4))

plt.boxplot(
    [
        temp[y == 0],  # Pas de panne
        temp[y == 1]   # Panne
    ],
    labels=["Pas de panne", "Panne"]
)

plt.ylabel("Air temperature [K]")
plt.title("Distribution de la température de l'air selon l’état de la machine")
plt.show()
