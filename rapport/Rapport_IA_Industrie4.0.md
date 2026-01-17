# IA et Industrie 4.0 : Transformation des Métiers

---

<div align="center">

## 📘 RAPPORT DE FIN DE MODULE

### Compétences en Intelligence Artificielle

---

**Titre du Projet**

# IA et Industrie 4.0

**Thème : Transformation des Métiers**

---

**Étudiant(s)**  
MEZOUAHI Kaoutar  
AGOURARI Ossama

**Encadrant / Professeur**  
[Nom du Professeur]

**Module**  
Compétences en IA

**Date**  
Janvier 2026

---

</div>

---

## Table des Matières

1. [Introduction](#introduction)
2. [Partie 1 : Industrie 4.0 – Concepts Clés](#partie-1--industrie-40--concepts-clés)
   - 2.1 Définition de l'Industrie 4.0
   - 2.2 Les Piliers Technologiques
   - 2.3 L'Internet des Objets (IoT)
   - 2.4 Big Data et Cloud Computing
   - 2.5 Intelligence Artificielle et Machine Learning
   - 2.6 Cybersécurité Industrielle
3. [Partie 2 : Robots et IA dans les Usines](#partie-2--robots-et-ia-dans-les-usines)
   - 3.1 Types de Robots Industriels
   - 3.2 Comment l'IA Transforme les Usines
   - 3.3 Applications Majeures de l'IA
4. [Partie 3 : Transformation des Métiers](#partie-3--transformation-des-métiers)
   - 4.1 Métiers Modifiés et Remplacés
   - 4.2 Nouveaux Métiers Créés
   - 4.3 Compétences Nécessaires
5. [Partie 4 : Étude de Cas Pratique](#partie-4--étude-de-cas-pratique)
   - 5.1 Maintenance Prédictive avec MLP
   - 5.2 Contrôle Qualité avec CNN
6. [Partie 5 : Analyse et Discussion](#partie-5--analyse-et-discussion)
   - 6.1 Comparaison MLP vs CNN
   - 6.2 Limites des Modèles
   - 6.3 Impacts Humains et Organisationnels
   - 6.4 Éthique et Formation
7. [Conclusion](#conclusion)
8. [Bibliographie](#bibliographie)
9. [Annexes](#annexes)

---

<div style="page-break-after: always;"></div>

## Introduction

### Contexte et Motivation

L'industrie mondiale connaît actuellement une transformation profonde, qualifiée de **quatrième révolution industrielle** ou **Industrie 4.0**. Cette révolution est caractérisée par l'intégration massive des technologies numériques dans les processus de production, notamment l'intelligence artificielle (IA), l'Internet des objets (IoT), le Big Data et la robotique avancée.

Selon le **World Economic Forum** (2023), plus de 85 millions d'emplois pourraient être déplacés d'ici 2025 en raison de l'automatisation, tandis que 97 millions de nouveaux rôles pourraient émerger, nécessitant de nouvelles compétences adaptées à cette transformation digitale.

### Définition de l'Industrie 4.0

L'**Industrie 4.0** désigne la numérisation complète des processus industriels, permettant une production plus flexible, efficace et personnalisée. Elle repose sur l'interconnexion des machines, des systèmes et des produits via des technologies de pointe, créant ainsi des **usines intelligentes** (Smart Factories).

Les caractéristiques principales de l'Industrie 4.0 sont :
- **Interconnexion** : Communication entre machines, systèmes et humains
- **Transparence de l'information** : Accès en temps réel aux données de production
- **Assistance technique** : Systèmes cyber-physiques aidant les humains
- **Décisions décentralisées** : Capacité des machines à prendre des décisions autonomes

### Rôle de l'IA dans les Usines

L'intelligence artificielle joue un rôle central dans cette transformation en permettant :
- L'analyse prédictive des données de production
- L'automatisation intelligente des processus
- Le contrôle qualité automatisé par vision industrielle
- L'optimisation continue des chaînes de montage

### Pourquoi les Métiers Changent Aujourd'hui

La convergence de l'IA, de la robotique et de l'automatisation transforme radicalement le paysage professionnel industriel. Les métiers traditionnels évoluent, certains disparaissent, tandis que de nouveaux rôles émergent, nécessitant des compétences en data science, cybersécurité et programmation.

### Objectif de ce Rapport

Ce rapport vise à étudier l'impact des robots et de l'intelligence artificielle dans les usines modernes. Nous illustrerons cette transformation à travers **deux exemples pratiques** :
1. La **maintenance prédictive** avec un modèle **MLP** (Multi-Layer Perceptron)
2. L'**inspection visuelle** pour le contrôle qualité avec un **CNN** (Convolutional Neural Network)

---

<div style="page-break-after: always;"></div>

## Partie 1 : Industrie 4.0 – Concepts Clés

### 2.1 Définition de l'Industrie 4.0

L'Industrie 4.0, également appelée **quatrième révolution industrielle**, représente une nouvelle ère de production manufacturière caractérisée par :

| Révolution | Période | Caractéristiques |
|------------|---------|------------------|
| Industrie 1.0 | 1784 | Mécanisation, machine à vapeur |
| Industrie 2.0 | 1870 | Production de masse, électricité |
| Industrie 3.0 | 1969 | Automatisation, électronique, informatique |
| **Industrie 4.0** | **2011** | **Usines intelligentes, IoT, IA, Big Data** |

*Tableau 1 : Les quatre révolutions industrielles*

Le terme "Industrie 4.0" a été introduit pour la première fois lors de la **Foire de Hanovre en 2011** par le gouvernement allemand, dans le cadre de sa stratégie de haute technologie.

### 2.2 Les Piliers Technologiques

L'Industrie 4.0 repose sur **neuf piliers technologiques** fondamentaux :

```
┌─────────────────────────────────────────────────────────────┐
│                    INDUSTRIE 4.0                            │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │     IoT     │  │  Big Data   │  │    Cloud    │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  Robotique  │  │     IA      │  │  Simulation │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Cybersécurité│ │  Intégration │ │ Fabrication │         │
│  │             │  │   Systèmes   │  │  Additive   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

*Figure 1 : Les neuf piliers de l'Industrie 4.0*

### 2.3 L'Internet des Objets (IoT)

L'**Internet des Objets Industriel (IIoT)** connecte les machines, capteurs et systèmes de production pour collecter et partager des données en temps réel.

**Applications de l'IoT industriel :**
- **Capteurs de vibration** : Surveillance de l'état des machines
- **Capteurs de température** : Contrôle des conditions de production
- **Capteurs de pression** : Monitoring des systèmes hydrauliques
- **RFID et codes-barres** : Traçabilité des produits

**Exemple concret :**
> Selon **Siemens** (2023), l'usine d'Amberg en Allemagne utilise plus de 1 000 capteurs IoT par ligne de production, permettant une traçabilité à 100% et un taux de qualité de 99,99%.

### 2.4 Big Data et Cloud Computing

Le **Big Data** industriel génère d'énormes volumes de données provenant des capteurs, machines et processus. Ces données sont caractérisées par les **5V** :

1. **Volume** : Téraoctets de données générées quotidiennement
2. **Vélocité** : Flux de données en temps réel
3. **Variété** : Données structurées, semi-structurées et non structurées
4. **Véracité** : Qualité et fiabilité des données
5. **Valeur** : Insights exploitables pour l'optimisation

**Le Cloud Computing** permet de :
- Stocker et traiter ces données massives
- Accéder aux applications de n'importe où
- Réduire les coûts d'infrastructure IT
- Faciliter la collaboration inter-sites

### 2.5 Intelligence Artificielle et Machine Learning

L'**intelligence artificielle** transforme les données brutes en informations exploitables grâce à :

**Types d'apprentissage :**

| Type | Description | Application industrielle |
|------|-------------|--------------------------|
| Supervisé | Apprentissage à partir de données étiquetées | Classification de défauts |
| Non supervisé | Découverte de patterns sans labels | Détection d'anomalies |
| Renforcement | Apprentissage par essai-erreur | Optimisation de processus |

*Tableau 2 : Types d'apprentissage automatique en industrie*

**Technologies IA en production :**
- **Machine Learning** : Prédiction de pannes, optimisation
- **Deep Learning** : Vision industrielle, reconnaissance de patterns
- **Natural Language Processing** : Analyse de rapports de maintenance
- **Computer Vision** : Inspection qualité automatisée

### 2.6 Cybersécurité Industrielle

La connectivité accrue expose les usines à de nouveaux risques cybernétiques. La **cybersécurité industrielle** protège :

- Les systèmes de contrôle (SCADA, PLC)
- Les données de production
- Les communications machine-to-machine
- La propriété intellectuelle

**Statistiques clés (IBM Security, 2023) :**
> Le coût moyen d'une violation de données dans le secteur manufacturier est de **4,47 millions de dollars**.

---

<div style="page-break-after: always;"></div>

## Partie 2 : Robots et IA dans les Usines

### 3.1 Types de Robots Industriels

L'industrie moderne utilise différents types de robots, chacun adapté à des tâches spécifiques :

#### 3.1.1 Robots Industriels Traditionnels

Ces robots effectuent des tâches répétitives avec précision dans des zones sécurisées.

| Caractéristique | Description |
|-----------------|-------------|
| **Fonction** | Assemblage, soudage, peinture, manutention |
| **Exemple** | FANUC, KUKA, ABB |
| **Avantage** | Haute précision, vitesse, endurance |
| **Inconvénient** | Cage de sécurité requise |

**Cas d'utilisation :** Dans les usines automobiles **BMW** et **Tesla**, des centaines de robots KUKA et FANUC assemblent les carrosseries avec une précision millimétrique.

#### 3.1.2 Cobots (Robots Collaboratifs)

Les **cobots** travaillent aux côtés des humains sans barrière de sécurité.

| Caractéristique | Description |
|-----------------|-------------|
| **Fonction** | Assistance aux opérateurs, tâches légères |
| **Exemple** | Universal Robots (UR3, UR5, UR10) |
| **Avantage** | Flexible, facile à programmer |
| **Inconvénient** | Charge utile limitée |

**Cas d'utilisation :** Chez **L'Oréal**, les cobots Universal Robots assistent les opérateurs dans l'emballage des produits cosmétiques, réduisant la fatigue et améliorant l'ergonomie.

#### 3.1.3 AGV (Automated Guided Vehicles)

Les **véhicules à guidage automatique** transportent des matériaux dans l'usine.

| Caractéristique | Description |
|-----------------|-------------|
| **Fonction** | Logistique interne, transport de pièces |
| **Exemple** | Amazon Robotics, Mobile Industrial Robots |
| **Avantage** | Optimisation des flux, fonctionnement 24/7 |
| **Inconvénient** | Infrastructure de navigation requise |

**Cas d'utilisation :** **Amazon** utilise plus de 750 000 robots dans ses entrepôts pour le tri et la livraison des colis.

#### 3.1.4 Drones Industriels

Les **drones** sont utilisés pour l'inspection et la surveillance.

| Caractéristique | Description |
|-----------------|-------------|
| **Fonction** | Inspection d'infrastructures, inventaire |
| **Exemple** | DJI Enterprise, Flyability |
| **Avantage** | Accès zones difficiles, rapidité |
| **Inconvénient** | Autonomie limitée, réglementation |

**Cas d'utilisation :** **Shell** utilise des drones pour inspecter ses raffineries, réduisant les risques pour les techniciens.

### 3.2 Comment l'IA Transforme les Usines

L'intégration de l'IA dans la robotique permet des capacités avancées :

```
┌────────────────────────────────────────────────────────────┐
│           INTÉGRATION IA + ROBOTIQUE                       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────────┐      ┌──────────────┐                   │
│  │   CAPTEURS   │──────│   DONNÉES    │                   │
│  └──────────────┘      └──────────────┘                   │
│         │                     │                            │
│         ▼                     ▼                            │
│  ┌──────────────────────────────────────┐                 │
│  │          INTELLIGENCE ARTIFICIELLE    │                 │
│  │  ┌────────────┐  ┌────────────┐      │                 │
│  │  │  Analyse   │  │  Décision  │      │                 │
│  │  └────────────┘  └────────────┘      │                 │
│  └──────────────────────────────────────┘                 │
│         │                     │                            │
│         ▼                     ▼                            │
│  ┌──────────────┐      ┌──────────────┐                   │
│  │   ACTION     │      │ OPTIMISATION │                   │
│  └──────────────┘      └──────────────┘                   │
└────────────────────────────────────────────────────────────┘
```

*Figure 2 : Cycle d'intégration IA et robotique*

### 3.3 Applications Majeures de l'IA

#### 🔧 1. Maintenance Prédictive

L'IA analyse les données des capteurs pour prédire les pannes avant qu'elles ne surviennent.

**Principe :**
- Collecte de données de capteurs (vibration, température, pression)
- Analyse par algorithmes de Machine Learning
- Prédiction de la durée de vie restante (RUL - Remaining Useful Life)
- Planification optimale des interventions

**Bénéfices :**
- Réduction de 10-40% des coûts de maintenance
- Diminution de 50% des temps d'arrêt imprévus
- Augmentation de 20-25% de la durée de vie des équipements

**Vidéo de référence :** *"Predictive Maintenance Using Deep Learning"* (MATLAB, 2023) - Cette vidéo illustre l'utilisation du Deep Learning pour analyser les données vibratoires et prédire les défaillances de machines.

#### 👁️ 2. Contrôle Qualité Automatisé

Les systèmes de **vision industrielle** combinés à l'IA détectent automatiquement les défauts.

**Composants :**
- Caméras haute résolution
- Éclairage optimisé
- Algorithmes CNN pour la classification d'images
- Système de rejet automatique

**Bénéfices :**
- Inspection 100% des produits (vs échantillonnage)
- Détection de défauts microscopiques
- Traçabilité complète
- Fonctionnement 24/7 sans fatigue

#### ⚡ 3. Optimisation de la Production

L'IA optimise les chaînes de montage en temps réel.

**Applications :**
- Planification dynamique de la production
- Équilibrage des lignes de production
- Réduction des déchets et rebuts
- Optimisation énergétique

**Exemple : Plateforme O3ai (Obeikan Digital Solutions)**
> La plateforme O3ai, basée sur **Microsoft Azure** et l'IoT industriel, a permis :
> - Augmentation de 30% de l'efficacité des équipements
> - Réduction de 12% des déchets de production
> - Transition vers la maintenance prédictive

#### 🛡️ 4. Sécurité et Prévention des Accidents

L'IA améliore la sécurité des travailleurs.

**Applications :**
- Détection du port des EPI (casque, gilet, lunettes)
- Surveillance des zones dangereuses
- Alertes en temps réel
- Analyse comportementale

---

<div style="page-break-after: always;"></div>

## Partie 3 : Transformation des Métiers

### 4.1 Métiers Modifiés et Remplacés

L'automatisation et l'IA impactent significativement les métiers industriels traditionnels :

**Métiers en transformation :**

| Métier Traditionnel | Évolution avec l'IA |
|---------------------|---------------------|
| Opérateur de ligne | Superviseur de systèmes automatisés |
| Technicien de maintenance | Analyste maintenance prédictive |
| Contrôleur qualité | Opérateur de vision industrielle |
| Magasinier | Gestionnaire de robots logistiques |
| Soudeur manuel | Programmeur de robots de soudage |

*Tableau 3 : Évolution des métiers industriels*

**Statistiques (McKinsey, 2023) :**
> D'ici 2030, environ **14%** de la main-d'œuvre mondiale pourrait avoir besoin de changer de catégorie professionnelle.

### 4.2 Nouveaux Métiers Créés

L'Industrie 4.0 génère de nouveaux métiers à haute valeur ajoutée :

#### 📊 Data Analyst Industriel

**Responsabilités :**
- Analyse des données de production
- Création de tableaux de bord
- Identification d'opportunités d'optimisation
- Communication des insights aux équipes

**Compétences requises :** Python, SQL, Power BI, statistiques

#### 🤖 Ingénieur Robotique

**Responsabilités :**
- Conception et programmation de robots
- Intégration des systèmes robotiques
- Maintenance avancée des robots
- Optimisation des cycles de production

**Compétences requises :** ROS, C++, Python, mécatronique

#### 🌐 Technicien IoT

**Responsabilités :**
- Installation et configuration des capteurs
- Gestion des réseaux industriels
- Maintenance des systèmes connectés
- Collecte et validation des données

**Compétences requises :** Réseaux, protocoles industriels, électronique

#### 🔐 Expert Cybersécurité Industrielle

**Responsabilités :**
- Protection des systèmes industriels
- Audit de sécurité
- Réponse aux incidents
- Formation des équipes

**Compétences requises :** Sécurité OT/IT, normes IEC 62443, pentesting

### 4.3 Compétences Nécessaires

Pour réussir dans l'Industrie 4.0, les professionnels doivent développer des compétences clés :

```
┌──────────────────────────────────────────────────────────┐
│          COMPÉTENCES INDUSTRIE 4.0                       │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  TECHNIQUES                    TRANSVERSALES             │
│  ┌────────────────────┐       ┌────────────────────┐    │
│  │ ▪ Python, R        │       │ ▪ Résolution de    │    │
│  │ ▪ Machine Learning │       │   problèmes        │    │
│  │ ▪ Robotique (ROS)  │       │ ▪ Communication    │    │
│  │ ▪ IoT, réseaux     │       │ ▪ Adaptabilité     │    │
│  │ ▪ Cybersécurité    │       │ ▪ Travail d'équipe │    │
│  │ ▪ Data Analysis    │       │ ▪ Pensée critique  │    │
│  └────────────────────┘       └────────────────────┘    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

*Figure 3 : Compétences requises pour l'Industrie 4.0*

### Lien avec Notre Étude de Cas

> "La maintenance prédictive, que nous illustrons avec notre modèle MLP, réduit le rôle des techniciens en intervention réactive et crée un nouveau rôle de **supervision IA**. De même, notre modèle CNN pour le contrôle qualité transforme le métier de contrôleur qualité en opérateur de systèmes de vision industrielle."

---

<div style="page-break-after: always;"></div>

## Partie 4 : Étude de Cas Pratique

Dans cette partie, nous présentons deux applications concrètes de l'IA dans l'industrie, développées dans le cadre de ce projet.

---

### 5.1 Maintenance Prédictive avec MLP

#### 5.1.1 Contexte et Problème Industriel

Les pannes imprévues de machines représentent un coût majeur pour l'industrie :
- **Temps d'arrêt non planifié** : Perte de production
- **Coûts de réparation d'urgence** : Pièces détachées, heures supplémentaires
- **Impact sur la qualité** : Produits défectueux potentiels
- **Sécurité** : Risques pour les opérateurs

**Objectif :** Développer un modèle capable de prédire les pannes machines à partir des données de capteurs, permettant une maintenance proactive plutôt que réactive.

#### 5.1.2 Dataset AI4I 2020

Le dataset **AI4I 2020 Predictive Maintenance Dataset** (UCI Machine Learning Repository) simule des données réalistes de machines industrielles.

**Caractéristiques du dataset :**

| Attribut | Description | Unité |
|----------|-------------|-------|
| UDI | Identifiant unique | - |
| Product ID | Identifiant produit | - |
| Type | Qualité du produit (L, M, H) | - |
| Air temperature | Température ambiante | K |
| Process temperature | Température de processus | K |
| Rotational speed | Vitesse de rotation | rpm |
| Torque | Couple | Nm |
| Tool wear | Usure de l'outil | min |
| **Machine failure** | **Indicateur de panne (cible)** | 0/1 |

*Tableau 4 : Description des variables du dataset AI4I 2020*

**Statistiques du dataset :**
- **Taille** : 10 000 observations
- **Distribution des pannes** : ~3.4% de pannes (classe déséquilibrée)
- **Types de pannes** : TWF, HDF, PWF, OSF, RNF

#### 5.1.3 Prétraitement des Données

Le prétraitement suit les étapes suivantes :

**1. Nettoyage des données :**
```python
# Suppression des colonnes non pertinentes
df = df.drop(columns=['UDI', 'Product ID'])
```

**2. Encodage des variables catégorielles :**
```python
# Encodage one-hot pour la variable 'Type'
df = pd.get_dummies(df, columns=['Type'], drop_first=True)
```

**3. Séparation features/target :**
```python
# X contient toutes les variables sauf 'Machine failure'
X = df.drop(columns=['Machine failure'])
# y est la variable cible
y = df['Machine failure']
```

**4. Normalisation :**
```python
# Standardisation des features (moyenne=0, écart-type=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

**5. Division train/test :**
```python
# 80% entraînement, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
```

#### 5.1.4 Architecture du Modèle MLP

Le **Multi-Layer Perceptron (MLP)** est un réseau de neurones artificiels composé de plusieurs couches de neurones.

**Configuration du modèle :**

```python
model = MLPClassifier(
    hidden_layer_sizes=(32, 16),  # 2 couches cachées
    activation='relu',            # Fonction d'activation ReLU
    max_iter=500,                 # Nombre maximal d'itérations
    random_state=42               # Reproductibilité
)
```

**Architecture détaillée :**

```
┌─────────────────────────────────────────────────────────┐
│                 ARCHITECTURE MLP                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  COUCHE D'ENTRÉE                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  11 neurones (features après encodage)           │   │
│  │  [Temp_Air, Temp_Process, Speed, Torque,        │   │
│  │   Wear, TWF, HDF, PWF, OSF, RNF, Type_M, Type_H] │   │
│  └─────────────────────────────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│  COUCHE CACHÉE 1                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  32 neurones + ReLU                              │   │
│  └─────────────────────────────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│  COUCHE CACHÉE 2                                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │  16 neurones + ReLU                              │   │
│  └─────────────────────────────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│  COUCHE DE SORTIE                                       │
│  ┌─────────────────────────────────────────────────┐   │
│  │  1 neurone (probabilité de panne)                │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

*Figure 4 : Architecture du modèle MLP*

**Fonction d'activation ReLU :**
f(x) = max(0, x)

Cette fonction permet d'introduire de la non-linéarité tout en évitant le problème du gradient qui disparaît.

#### 5.1.5 Résultats et Métriques

Après entraînement sur 80% des données et test sur 20%, nous obtenons :

**Accuracy globale : ~97%**

**Matrice de confusion :**

```
                 Prédiction
                  0      1
Réel    0     [1920     5]
        1     [  52    23]
```

*Figure 5 : Matrice de confusion du modèle MLP*

**Rapport de classification :**

| Classe | Précision | Rappel | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| 0 (Pas de panne) | 0.97 | 1.00 | 0.98 | 1925 |
| 1 (Panne) | 0.82 | 0.31 | 0.45 | 75 |
| **Moyenne** | **0.97** | **0.97** | **0.96** | **2000** |

*Tableau 5 : Rapport de classification du modèle MLP*

#### 5.1.6 Interprétation des Résultats

**Points forts :**
- Excellente identification des machines fonctionnelles (précision 97%)
- Très peu de fausses alertes (5 faux positifs)

**Points à améliorer :**
- Le rappel pour la classe "panne" est de 31%, ce qui signifie que 69% des pannes ne sont pas détectées
- Ce déséquilibre est dû à la rareté des événements de panne dans le dataset (3.4%)

**Solutions possibles :**
- Techniques de rééquilibrage (SMOTE, under-sampling)
- Ajustement du seuil de décision
- Utilisation d'une fonction de perte pondérée

#### 5.1.7 Impact sur les Métiers

**Transformation du rôle du technicien :**

| Avant (Maintenance Réactive) | Après (Maintenance Prédictive) |
|------------------------------|--------------------------------|
| Intervention après panne | Intervention préventive planifiée |
| Diagnostic manuel | Analyse assistée par IA |
| Pièces de rechange en urgence | Stock optimisé par prédiction |
| Temps d'arrêt imprévus | Arrêts planifiés minimaux |

*Tableau 6 : Évolution du métier de technicien de maintenance*

**Nouveau workflow :**
1. Le système IA analyse en continu les données capteurs
2. Une alerte est générée avant la panne potentielle
3. Le technicien planifie l'intervention optimale
4. La maintenance est effectuée pendant un arrêt programmé

---

### 5.2 Contrôle Qualité avec CNN

#### 5.2.1 Contexte et Problème Industriel

Le contrôle qualité est essentiel dans l'industrie pour :
- Garantir la conformité des produits
- Réduire les coûts de non-qualité
- Satisfaire les exigences clients
- Assurer la sécurité des utilisateurs finaux

**Limite du contrôle manuel :**
- Fatigue visuelle des opérateurs
- Subjectivité des inspections
- Impossibilité de contrôler 100% des pièces
- Coût élevé de la main-d'œuvre

**Objectif :** Développer un système de vision industrielle capable de classifier automatiquement les pièces de fonderie comme "OK" ou "DÉFAUT".

#### 5.2.2 Dataset Casting Quality Inspection

Le dataset utilisé provient de **Kaggle** et contient des images de pièces de fonderie (casting).

**Structure du dataset :**
```
casting_data/
├── train/
│   ├── def_front/    (images avec défauts)
│   └── ok_front/     (images conformes)
└── test/
    ├── def_front/
    └── ok_front/
```

**Caractéristiques :**

| Attribut | Valeur |
|----------|--------|
| Images d'entraînement | 6 634 |
| Images de test | 715 |
| Classes | 2 (OK / DÉFAUT) |
| Format | JPEG, 300×300 pixels |
| Type de défauts | Défauts de surface, porosités |

*Tableau 7 : Caractéristiques du dataset Casting*

#### 5.2.3 Architecture du Modèle CNN

Le **Convolutional Neural Network (CNN)** est particulièrement adapté pour l'analyse d'images grâce à ses capacités d'extraction automatique de caractéristiques.

**Architecture développée :**

```python
model = models.Sequential([
    # Bloc 1
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(250,250,3)),
    layers.MaxPooling2D((2,2)),
    
    # Bloc 2
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    # Bloc 3
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    # Bloc 4
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    # Classification
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
```

**Visualisation de l'architecture :**

```
┌──────────────────────────────────────────────────────────┐
│                 ARCHITECTURE CNN                         │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  INPUT: Image 250×250×3 (RGB)                           │
│                    │                                     │
│                    ▼                                     │
│  ┌──────────────────────────────────────┐               │
│  │ CONV2D 32 filtres (3×3) + ReLU       │               │
│  │ MaxPooling (2×2)                      │               │
│  │ Output: 124×124×32                    │               │
│  └──────────────────────────────────────┘               │
│                    │                                     │
│                    ▼                                     │
│  ┌──────────────────────────────────────┐               │
│  │ CONV2D 64 filtres (3×3) + ReLU       │               │
│  │ MaxPooling (2×2)                      │               │
│  │ Output: 61×61×64                      │               │
│  └──────────────────────────────────────┘               │
│                    │                                     │
│                    ▼                                     │
│  ┌──────────────────────────────────────┐               │
│  │ CONV2D 128 filtres (3×3) + ReLU      │               │
│  │ MaxPooling (2×2)                      │               │
│  │ Output: 29×29×128                     │               │
│  └──────────────────────────────────────┘               │
│                    │                                     │
│                    ▼                                     │
│  ┌──────────────────────────────────────┐               │
│  │ CONV2D 128 filtres (3×3) + ReLU      │               │
│  │ MaxPooling (2×2)                      │               │
│  │ Output: 13×13×128                     │               │
│  └──────────────────────────────────────┘               │
│                    │                                     │
│                    ▼                                     │
│  ┌──────────────────────────────────────┐               │
│  │ FLATTEN: 21632 neurones              │               │
│  │ DENSE: 512 neurones + ReLU           │               │
│  │ DENSE: 1 neurone + Sigmoid           │               │
│  └──────────────────────────────────────┘               │
│                    │                                     │
│                    ▼                                     │
│  OUTPUT: Probabilité [0-1] (DÉFAUT / OK)                │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

*Figure 6 : Architecture du modèle CNN*

#### 5.2.4 Configuration de l'Entraînement

**Paramètres d'entraînement :**

| Paramètre | Valeur |
|-----------|--------|
| Optimiseur | Adam |
| Fonction de perte | Binary Crossentropy |
| Taille des batches | 16 |
| Nombre d'epochs | 10 |
| Taille d'image | 250×250 pixels |
| Normalisation | Division par 255 |

*Tableau 8 : Paramètres d'entraînement du CNN*

**Compilation du modèle :**
```python
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
```

#### 5.2.5 Résultats et Performances

**Performances finales :**

| Métrique | Valeur |
|----------|--------|
| **Accuracy (validation)** | **99.86%** |
| Temps d'entraînement | 86 min 54 sec |
| Temps de prédiction par image | < 1 seconde |

*Tableau 9 : Performances du modèle CNN*

**Courbes d'apprentissage :**

L'évolution de l'accuracy et de la loss au cours des epochs montre :
- Une convergence rapide du modèle
- Pas de surapprentissage significatif (validation proche de l'entraînement)
- Stabilité des performances après 8-10 epochs

#### 5.2.6 Interprétation et Validation

**Test sur images individuelles :**

Le modèle a été validé sur des images de test, démontrant sa capacité à :
- Identifier correctement les pièces conformes
- Détecter les défauts de surface et porosités
- Généraliser sur des images non vues pendant l'entraînement

**Exemple de prédiction :**
- Image de test : `cast_def_0_242.jpeg`
- Prédiction du modèle : **DÉFAUT** ✓

#### 5.2.7 Applications Industrielles

Ce modèle peut être déployé pour :

1. **Inspection automatique 24/7** : Fonctionnement continu sans fatigue
2. **Détection rapide** : Temps de prédiction < 1 seconde par pièce
3. **Réduction des coûts** : Moins de rebuts, moins de contrôles manuels
4. **Traçabilité** : Enregistrement automatique de chaque inspection

**Impact sur les métiers :**

| Avant (Contrôle Manuel) | Après (Vision IA) |
|-------------------------|-------------------|
| Inspection par échantillonnage | Contrôle 100% |
| Décision subjective | Classification objective |
| Fatigue visuelle | Fonctionnement 24/7 |
| Documentation manuelle | Traçabilité automatique |

*Tableau 10 : Évolution du contrôle qualité*

---

<div style="page-break-after: always;"></div>

## Partie 5 : Analyse et Discussion

### 6.1 Comparaison MLP vs CNN

Les deux modèles développés illustrent différentes approches de l'IA en industrie :

| Critère | MLP (Maintenance) | CNN (Qualité) |
|---------|-------------------|---------------|
| **Type de données** | Données tabulaires (capteurs) | Images |
| **Architecture** | Perceptron multicouche | Réseau convolutionnel |
| **Complexité** | Modérée (< 1000 paramètres) | Élevée (millions de paramètres) |
| **Temps d'entraînement** | Quelques secondes | ~87 minutes |
| **Accuracy** | ~97% | ~99.86% |
| **Interprétabilité** | Modérée | Faible (boîte noire) |
| **Application** | Prédiction de pannes | Classification d'images |

*Tableau 11 : Comparaison des modèles MLP et CNN*

**Choix du modèle selon le contexte :**
- **MLP** : Idéal pour des données structurées issues de capteurs
- **CNN** : Indispensable pour l'analyse d'images et la vision industrielle

### 6.2 Limites des Modèles

#### Limites du modèle MLP :
1. **Déséquilibre des classes** : Peu de pannes dans le dataset (3.4%)
2. **Faible rappel** : 31% des pannes détectées seulement
3. **Données simulées** : Le dataset AI4I 2020 simule des conditions réelles mais reste synthétique
4. **Généralisation** : Performance à valider sur des données réelles d'usine

#### Limites du modèle CNN :
1. **Ressources computationnelles** : Nécessite un GPU pour l'entraînement
2. **Temps d'entraînement** : ~87 minutes vs quelques secondes pour le MLP
3. **Types de défauts** : Classification binaire uniquement (OK/DÉFAUT)
4. **Conditions d'éclairage** : Sensibilité aux variations d'éclairage

### 6.3 Impacts Humains et Organisationnels

#### Impacts positifs :
- **Amélioration des conditions de travail** : Réduction des tâches répétitives
- **Montée en compétences** : Nouvelles responsabilités à plus haute valeur ajoutée
- **Sécurité renforcée** : Moins d'interventions d'urgence dangereuses
- **Productivité** : Efficacité accrue des processus

#### Défis organisationnels :
- **Résistance au changement** : Peur de l'automatisation
- **Formation** : Besoin de programmes de reconversion
- **Investissement** : Coûts d'implémentation des technologies
- **Transition** : Gestion du changement culturel

### 6.4 Éthique et Formation

#### Questions éthiques :
1. **Emploi** : Impact sur l'emploi des opérateurs peu qualifiés
2. **Vie privée** : Surveillance continue des performances
3. **Responsabilité** : Qui est responsable en cas d'erreur de l'IA ?
4. **Biais** : Risque de biais dans les algorithmes

#### Nécessité de formation :
- **Upskilling** : Former les employés actuels aux nouvelles technologies
- **Reskilling** : Reconversion vers de nouveaux métiers
- **Éducation continue** : Mise à jour régulière des compétences

---

<div style="page-break-after: always;"></div>

## Conclusion

### Résumé des Points Clés

Ce rapport a exploré la transformation de l'industrie par l'intelligence artificielle dans le contexte de l'**Industrie 4.0**. Les principales conclusions sont :

1. **L'Industrie 4.0** représente une révolution technologique majeure, caractérisée par l'intégration de l'IoT, du Big Data, de l'IA et de la robotique avancée dans les processus de production.

2. **Les robots et l'IA** transforment profondément les usines, avec des applications dans la maintenance prédictive, le contrôle qualité, l'optimisation de production et la sécurité.

3. **Les métiers évoluent** significativement : certains sont modifiés, d'autres remplacés, et de nouveaux rôles émergent (data analyst, ingénieur robotique, technicien IoT, expert cybersécurité).

4. **Nos études de cas** illustrent cette transformation :
   - Le modèle **MLP** pour la maintenance prédictive atteint 97% d'accuracy
   - Le modèle **CNN** pour le contrôle qualité atteint 99.86% d'accuracy

### Impacts Positifs et Nécessité d'Adaptation

L'IA et l'automatisation apportent des bénéfices significatifs :
- Réduction des coûts de maintenance et de non-qualité
- Amélioration de la productivité et de la sécurité
- Création de nouveaux métiers à haute valeur ajoutée

Cependant, ces changements nécessitent une **montée en compétences** des travailleurs et une gestion attentive de la transition pour assurer une transformation inclusive et éthique.

### Vision Future

Les usines du futur seront de plus en plus autonomes, avec :
- Des systèmes cyber-physiques auto-adaptatifs
- Une collaboration homme-machine optimisée
- Une production personnalisée et flexible
- Une empreinte environnementale réduite

**Le rôle humain évoluera** vers la supervision, l'analyse et la prise de décisions stratégiques, tandis que les tâches répétitives seront automatisées.

> "L'intelligence artificielle ne remplace pas l'humain, elle le complète et l'augmente."

---

<div style="page-break-after: always;"></div>

## Bibliographie

### Articles et Rapports Académiques

1. **World Economic Forum** (2023). *The Future of Jobs Report 2023*. Genève : WEF.

2. **McKinsey Global Institute** (2023). *The Next Normal in Manufacturing: The State of AI in 2023*. McKinsey & Company.

3. **IBM** (2023). *AI in Manufacturing: A Comprehensive Guide*. IBM Institute for Business Value.

4. **PwC** (2023). *Industry 4.0: Building the Digital Enterprise*. PricewaterhouseCoopers.

5. **Deloitte** (2023). *Smart Factories and the Future of Manufacturing*. Deloitte Insights.

### Sources Industrielles

6. **Siemens** (2023). *Industry 4.0 Overview*. Disponible sur : https://www.siemens.com/industry4.0

7. **ABB** (2023). *Robotics and Discrete Automation*. Rapport annuel.

8. **FANUC** (2023). *Factory Automation Solutions*. Documentation technique.

9. **Universal Robots** (2023). *Collaborative Robots in Manufacturing*. Livre blanc.

10. **International Federation of Robotics** (2023). *World Robotics Report 2023*.

### Vidéos de Référence

11. **MATLAB** (2023). *Predictive Maintenance Using Deep Learning* [Vidéo]. YouTube. https://www.youtube.com/watch?v=InMlOMcUzM4

12. **Reliability Academy** (2023). *Predictive Maintenance Explained* [Vidéo]. YouTube. https://www.youtube.com/watch?v=2_o1SDy6__U

13. **Microsoft** (2023). *O3ai - AI-Powered Manufacturing Platform* [Vidéo]. YouTube. https://www.youtube.com/watch?v=jjwIo6SZeZU

### Datasets

14. **AI4I 2020 Predictive Maintenance Dataset** - UCI Machine Learning Repository. https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset

15. **Casting Product Image Data for Quality Inspection** - Kaggle. https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product

### Documentation Technique

16. **TensorFlow** (2023). *Keras CNN Guide*. https://keras.io/guides/

17. **Scikit-learn** (2023). *MLPClassifier Documentation*. https://scikit-learn.org/

---

<div style="page-break-after: always;"></div>

## Annexes

### Annexe A : Code Python - Modèle MLP

```python
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
df = pd.get_dummies(df, columns=['Type'], drop_first=True)

# Séparation des X et y 
X = df.drop(columns=['Machine failure'])
y = df['Machine failure']

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Division train/test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Création du modèle MLPClassifier
model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation='relu',
    max_iter=500,
    random_state=42
)

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédiction
y_pred = model.predict(X_test)

# Évaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
```

### Annexe B : Code Python - Modèle CNN

```python
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os

# Chemins des données
chemin_base = "path/to/casting_data"

# Chargement des datasets
ds_train = tf.keras.utils.image_dataset_from_directory(
    os.path.join(chemin_base, "train"),
    image_size=(250, 250),
    batch_size=16
)

ds_test = tf.keras.utils.image_dataset_from_directory(
    os.path.join(chemin_base, "test"),
    image_size=(250, 250),
    batch_size=16
)

# Normalisation
normalisation = layers.Rescaling(1./255)
ds_train = ds_train.map(lambda x, y: (normalisation(x), y))
ds_test = ds_test.map(lambda x, y: (normalisation(x), y))

# Construction du modèle CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(250,250,3)),
    layers.MaxPooling2D((2,2)),
    
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),
    
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compilation
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Entraînement
history = model.fit(
    ds_train,
    epochs=10,
    validation_data=ds_test
)

# Évaluation
test_loss, test_acc = model.evaluate(ds_test)
print(f"Test accuracy: {test_acc:.4f}")
```

### Annexe C : Glossaire

| Terme | Définition |
|-------|------------|
| **IA** | Intelligence Artificielle - Capacité d'une machine à simuler l'intelligence humaine |
| **ML** | Machine Learning - Sous-domaine de l'IA permettant aux machines d'apprendre |
| **MLP** | Multi-Layer Perceptron - Réseau de neurones artificiels |
| **CNN** | Convolutional Neural Network - Réseau de neurones pour l'analyse d'images |
| **IoT** | Internet of Things - Réseau d'objets connectés |
| **Cobot** | Robot collaboratif travaillant aux côtés des humains |
| **AGV** | Automated Guided Vehicle - Véhicule à guidage automatique |
| **RUL** | Remaining Useful Life - Durée de vie restante |
| **SCADA** | Supervisory Control and Data Acquisition - Système de contrôle industriel |

---

**Fin du Rapport**

---

*Rapport rédigé dans le cadre du module "Compétences en IA"*  
*Thème : Transformation des Métiers - IA et Industrie 4.0*  
*Date : Janvier 2026*
