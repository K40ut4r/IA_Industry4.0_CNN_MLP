---
marp: true
theme: default
paginate: true
header: 'IA et Industrie 4.0'
footer: 'Module : Compétences en IA - Janvier 2026'
---

# 🤖 IA et Industrie 4.0
## Transformation des Métiers

---

**MEZOUAHI Kaoutar**  
**AGOURARI Ossama**

*Module : Compétences en Intelligence Artificielle*

---

# 📋 Plan de la Présentation

1. Introduction à l'Industrie 4.0
2. Les piliers technologiques
3. Robots et IA dans les usines
4. Applications de l'IA industrielle
5. Transformation des métiers
6. **Étude de cas 1** : Maintenance prédictive (MLP)
7. **Étude de cas 2** : Contrôle qualité (CNN)
8. Analyse et Discussion
9. Conclusion

---

# 🏭 Slide 1 : Qu'est-ce que l'Industrie 4.0 ?

## Définition

L'**Industrie 4.0** est la **4ème révolution industrielle**, caractérisée par :

| Révolution | Année | Innovation clé |
|------------|-------|----------------|
| 1.0 | 1784 | Machine à vapeur |
| 2.0 | 1870 | Électricité |
| 3.0 | 1969 | Informatique |
| **4.0** | **2011** | **IA, IoT, Big Data** |

> **Objectif** : Créer des **usines intelligentes** (Smart Factories)

---

# ⚙️ Slide 2 : Les Piliers de l'Industrie 4.0

```
┌────────────────────────────────────────────┐
│           9 PILIERS TECHNOLOGIQUES         │
├────────────────────────────────────────────┤
│   IoT        │   Big Data   │   Cloud      │
├────────────────────────────────────────────┤
│   Robotique  │   IA / ML    │   Simulation │
├────────────────────────────────────────────┤
│   Cybersécurité │ Intégration │ Impression 3D │
└────────────────────────────────────────────┘
```

**Clé du succès** : L'interconnexion de tous ces piliers

---

# 🤖 Slide 3 : Types de Robots Industriels

| Type | Fonction | Exemple |
|------|----------|---------|
| **Robot industriel** | Soudage, assemblage | FANUC, KUKA |
| **Cobot** | Collaboration humain-robot | Universal Robots |
| **AGV** | Transport automatisé | Amazon Robotics |
| **Drone** | Inspection, surveillance | DJI Enterprise |

> **750 000+** robots utilisés par Amazon dans ses entrepôts

---

# 🌟 Slide 4 : Applications de l'IA dans l'Industrie

## 4 Applications Majeures

| Application | Bénéfice |
|-------------|----------|
| 🔧 **Maintenance prédictive** | -50% temps d'arrêt |
| ��️ **Contrôle qualité** | Inspection 100% |
| ⚡ **Optimisation production** | +30% efficacité |
| 🛡️ **Sécurité** | Détection EPI en temps réel |

---

# 📊 Slide 5 : Maintenance Prédictive - Concept

## Comparaison des Stratégies

| Type | Description | Coût |
|------|-------------|------|
| **Réactive** | Réparer après panne | 💰💰💰 Très élevé |
| **Préventive** | Planning fixe | 💰💰 Modéré |
| **Prédictive** | IA prédit la panne | 💰 Optimisé |

> **Source** : Vidéo MATLAB "Predictive Maintenance Using Deep Learning"

---

# 👷 Slide 6 : Transformation des Métiers

## Avant vs Après l'IA

| Métier traditionnel | Évolution avec l'IA |
|---------------------|---------------------|
| Technicien maintenance | Analyste IA maintenance |
| Contrôleur qualité | Opérateur vision IA |
| Magasinier | Gestionnaire robots |
| Opérateur ligne | Superviseur automatisation |

## Nouveaux métiers créés
- 📊 Data Analyst industriel
- 🤖 Ingénieur robotique  
- 🌐 Technicien IoT
- 🔐 Expert cybersécurité

---

# 🧠 Slide 7 : Étude de Cas 1 - MLP

## Maintenance Prédictive avec MLPClassifier

**Dataset** : AI4I 2020 (10 000 observations)

**Variables** :
- Température air/processus
- Vitesse de rotation
- Couple et usure

**Architecture MLP** :
```
Entrée (11) → Couche 1 (32) → Couche 2 (16) → Sortie (1)
```

---

# 📈 Slide 8 : Résultats MLP

## Performance du Modèle

| Métrique | Valeur |
|----------|--------|
| **Accuracy** | **97%** |
| Précision (classe 0) | 97% |
| Rappel (classe 1) | 31% |

**Matrice de confusion** :
```
              Prédit
            0      1
Réel  0  [1920    5]
      1  [  52   23]
```

> **Impact** : Le technicien passe de la maintenance réactive à la supervision IA

---

# 👁️ Slide 9 : Étude de Cas 2 - CNN

## Contrôle Qualité avec CNN

**Dataset** : Casting Quality (Kaggle)
- 6 634 images d'entraînement
- 715 images de test
- Classes : OK / DÉFAUT

**Architecture CNN** :
```
Conv2D(32) → Conv2D(64) → Conv2D(128) → Conv2D(128) → Dense(512) → Output
```

---

# 🎯 Slide 10 : Résultats CNN

## Performance Exceptionnelle

| Métrique | Valeur |
|----------|--------|
| **Accuracy** | **99.86%** |
| Temps d'entraînement | 87 min |
| Temps prédiction | < 1 sec |

**Applications industrielles** :
- ✅ Inspection 24/7
- ✅ Détection automatique
- ✅ Traçabilité complète
- ✅ Réduction des rebuts

---

# ⚖️ Slide 11 : Comparaison MLP vs CNN

| Critère | MLP | CNN |
|---------|-----|-----|
| **Type données** | Capteurs (tabulaire) | Images |
| **Complexité** | Faible | Élevée |
| **Accuracy** | 97% | 99.86% |
| **Temps entraînement** | Secondes | ~87 min |
| **Application** | Maintenance | Vision qualité |

> **Conclusion** : Chaque modèle est adapté à son contexte

---

# 💡 Slide 12 : Limites et Perspectives

## Limites identifiées

**MLP** :
- Classes déséquilibrées (3.4% pannes)
- Faible rappel pour les pannes

**CNN** :
- Ressources GPU nécessaires
- Sensibilité à l'éclairage

## Améliorations futures
- Rééquilibrage SMOTE
- Transfer Learning
- Détection multi-classes

---

# 🎓 Slide 13 : Conclusion

## Points Clés

1. **L'Industrie 4.0** transforme profondément les usines
2. **L'IA** permet maintenance prédictive et vision automatisée
3. **Les métiers évoluent** vers plus de supervision et analyse
4. **Nos modèles** démontrent l'efficacité de l'IA :
   - MLP : 97% accuracy (maintenance)
   - CNN : 99.86% accuracy (qualité)

> **"L'IA ne remplace pas l'humain, elle l'augmente."**

---

# 📚 Slide 14 : Références

## Sources principales

- **World Economic Forum** - Future of Jobs Report 2023
- **McKinsey** - The Next Normal in Manufacturing
- **Siemens** - Industry 4.0 Overview
- **IBM** - AI in Manufacturing

## Vidéos utilisées
- MATLAB: Predictive Maintenance Using Deep Learning
- Microsoft: O3ai Platform
- Predictive Maintenance Explained

## Datasets
- AI4I 2020 (UCI ML Repository)
- Casting Quality (Kaggle)

---

# 🙏 Merci de votre attention !

## Questions ?

---

**MEZOUAHI Kaoutar** | **AGOURARI Ossama**

*Projet de Fin de Module - Compétences en IA*  
*Thème : Transformation des Métiers - IA et Industrie 4.0*

Janvier 2026
