
# Pipeline Collaborative d'Analyse de Sentiment

## Description du projet

Ce projet a été réalisé par une équipe de trois étudiants afin de construire un pipeline d'analyse de sentiment basé sur un modèle BERT. L'objectif était de diviser les différentes étapes en trois composants principaux et de collaborer en utilisant un workflow Git avec branches et Pull Requests.

## Structure du dépôt

```
.
├─ src/
│   ├─ data_extraction.py   # Extraction des données
│   ├─ data_processing.py   # Nettoyage et tokenisation des données
│   ├─ model.py             # Entraînement du modèle BERT
│   └─ inference.py         # Script d'inférence
├─ tests/
│   └─ unit/
│       ├─ test_data_extraction.py
│       ├─ test_data_processing.py
│       ├─ test_model.py
│       └─ test_inference.py
├─ requirements.txt         # Dépendances du projet
└─ README.md

```

## Répartition des tâches

Chaque étudiant a pris en charge une partie du projet comme suit :

### 1. Extraction de données (Étudiant 1)

-   Chargement des données brutes.
-   Gestion des erreurs (fichiers manquants, formats incorrects).
-   Implémentation des tests unitaires dans `tests/unit/test_data_extraction.py`.

### 2. Traitement des données (Étudiant 2)

-   Nettoyage du texte (suppression des caractères inutiles, mise en minuscules, normalisation).
-   Tokenisation des textes avec `AutoTokenizer` de Hugging Face.
-   Division des données en ensembles d'entraînement et de validation.
-   Implémentation des tests unitaires dans `tests/unit/test_data_processing.py`.

### 3. Entraînement et Inférence du modèle (Étudiant 3)

-   Chargement et fine-tuning d'un modèle `BERT` pré-entraîné.
-   Mise en place d'un script pour l'inférence (`inference.py`).
-   Implémentation des tests unitaires dans `tests/unit/test_model.py` et `tests/unit/test_inference.py`.

## Workflow de collaboration avec Git

Nous avons utilisé un workflow basé sur GitHub avec branches et Pull Requests :

### Branching

-   `feature-data-extraction` → Étudiant 1
-   `feature-data-processing` → Étudiant 2
-   `feature-model-training` → Étudiant 3
-   `feature-inference` → Étudiant 3 (optionnel)

### Pull Requests

-   Chaque branche a été fusionnée dans `main` via une Pull Request.
-   Chaque PR a été soumise à une revue de code par au moins un autre membre de l'équipe avant d'être fusionnée.

### Messages de Commit

Nous avons suivi une convention de messages descriptifs, par exemple :

-   `Ajout du chargeur de données CSV pour les données de sentiment`
-   `Implémentation de la tokenisation avec AutoTokenizer`
-   `Entraînement du modèle BERT et mise en place de l'inférence`

## Instructions d'installation et d'exécution

### Prérequis

-   Python 3.8+
-   pip
-   Virtualenv (optionnel)

### Installation

1.  Cloner le projet :
    
    ```bash
    git clone https://github.com/utilisateur/projet-sentiment-analysis.git
    cd projet-sentiment-analysis
    
    ```
    
2.  Créer un environnement virtuel et installer les dépendances :
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    pip install -r requirements.txt
    
    ```
    

### Exécution du pipeline

1.  Extraction des données :
    
    ```bash
    python src/data_extraction.py
    
    ```
    
2.  Traitement des données :
    
    ```bash
    python src/data_processing.py
    
    ```
    
3.  Entraînement du modèle :
    
    ```bash
    python src/model.py
    
    ```
    
4.  Inférence sur un texte :
    
    ```bash
    python src/inference.py "Votre texte ici"
    
    ```
    

## Tests

Nous avons inclus des tests unitaires pour valider chaque étape du pipeline. Pour exécuter les tests :

```bash
pytest tests/unit/

```

## Améliorations futures

-   Optimisation du modèle pour de meilleures performances.
-   Ajout d’une interface utilisateur pour une utilisation plus intuitive.
-   Intégration de nouveaux jeux de données pour une meilleure généralisation.

## Auteurs

-   Edouard (Extraction de données)
-   Anis (Traitement des données)
-   Yann (Modélisation et inférence)