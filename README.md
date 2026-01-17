# IA et Industrie 4.0 : Transformation des Métiers

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.x-green.svg)](https://scikit-learn.org/)

## 📋 Description du Projet

Ce projet est réalisé dans le cadre du module **"Compétences en Intelligence Artificielle"** et explore le thème de la **Transformation des Métiers** à travers l'étude de l'IA et de la robotique dans les usines (Industrie 4.0).

### 🎯 Objectif

Étudier les robots et l'IA dans les usines modernes à travers deux démonstrations pratiques :
1. **Maintenance prédictive** : Utilisation d'un MLP pour prédire les pannes machines
2. **Contrôle qualité automatisé** : Utilisation d'un CNN pour détecter les défauts

## 📁 Structure du Projet

```
IA_Industry4.0_CNN_MLP/
├── 📂 data/
│   ├── predictive_maintenance/
│   │   └── ai4i2020.csv                 # Dataset AI4I 2020
│   └── quality_control/
│       └── PCB_data/                    # Données contrôle qualité
├── 📂 notebooks/
│   ├── predictive_maintenance_MLP/
│   │   └── ai4i.py                      # Modèle MLP
│   └── quality_control_CNN_or_YOLO/
│       └── classification_binaire.ipynb  # Modèle CNN
├── 📂 rapport/
│   ├── Rapport_IA_Industrie4.0.md       # Rapport complet (~25 pages)
│   └── Presentation_IA_Industrie4.0.md  # Présentation (14 slides)
├── requirements.txt
└── README.md
```

## 🛠️ Technologies Utilisées

- **Python 3.8+**
- **scikit-learn** : MLPClassifier pour la maintenance prédictive
- **TensorFlow/Keras** : CNN pour le contrôle qualité
- **Pandas & NumPy** : Manipulation des données
- **Matplotlib** : Visualisation

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/K40ut4r/IA_Industry4.0_CNN_MLP.git
cd IA_Industry4.0_CNN_MLP

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation

### Modèle MLP - Maintenance Prédictive

```bash
cd notebooks/predictive_maintenance_MLP
python ai4i.py
```

**Résultats attendus :**
- Accuracy : ~97%
- Prédiction des pannes machines basée sur les données capteurs

### Modèle CNN - Contrôle Qualité

Ouvrir le notebook `classification_binaire.ipynb` dans Jupyter :

```bash
cd notebooks/quality_control_CNN_or_YOLO
jupyter notebook classification_binaire.ipynb
```

**Résultats attendus :**
- Accuracy : ~99.86%
- Classification automatique OK/DÉFAUT des pièces de fonderie

## 📊 Résumé des Modèles

| Modèle | Application | Dataset | Accuracy |
|--------|-------------|---------|----------|
| **MLP** | Maintenance prédictive | AI4I 2020 (10 000 obs.) | ~97% |
| **CNN** | Contrôle qualité | Casting (7 349 images) | ~99.86% |

## 📚 Documentation

- **[Rapport complet](rapport/Rapport_IA_Industrie4.0.md)** : Rapport académique (~25 pages) détaillant le contexte, les modèles et l'analyse
- **[Présentation](rapport/Presentation_IA_Industrie4.0.md)** : Slides de présentation (14 pages) au format Marp

## 📖 Références

### Vidéos
- [Predictive Maintenance Using Deep Learning - MATLAB](https://www.youtube.com/watch?v=InMlOMcUzM4)
- [Predictive Maintenance Explained](https://www.youtube.com/watch?v=2_o1SDy6__U)
- [O3ai - AI-Powered Manufacturing Platform](https://www.youtube.com/watch?v=jjwIo6SZeZU)

### Datasets
- [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)
- [Casting Product Image Data for Quality Inspection](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)

### Articles
- World Economic Forum - Future of Jobs Report 2023
- McKinsey - The Next Normal in Manufacturing
- IBM - AI in Manufacturing

## 👥 Auteurs

- **MEZOUAHI Kaoutar**
- **AGOURARI Ossama**

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

*Projet de Fin de Module - Compétences en IA*  
*Thème : Transformation des Métiers - IA et Industrie 4.0*  
*Date : Janvier 2026*
