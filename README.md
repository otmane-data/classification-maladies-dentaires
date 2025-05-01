Classification des Pathologies Dentaires avec Supervision via Docker, Prometheus et Grafana

Ce projet propose une application web de classification automatique de pathologies dentaires à partir d'images, enrichie par une supervision des métriques système et applicatives grâce à Prometheus et Grafana. Le tout est orchestré avec Docker Compose pour une installation simplifiée.

🔧 Technologies Utilisées

Python, Flask : application web

PyTorch : modèle de classification dentaire

Prometheus : collecte des métriques

Grafana : visualisation des métriques

Docker & Docker Compose : conteneurisation et orchestration

HTML/CSS : interface utilisateur

⚡ Prérequis

Docker

Docker Compose

🔄 Structure du projet

├── app.py                 # Application Flask principale
├── app_modified.py        # Version instrumentée avec Prometheus
├── Dockerfile             # Image Docker de l’application
├── docker-compose.yml     # Orchestration multi-conteneurs
├── models/                # Modèle de classification (PyTorch)
├── prometheus/            # Configuration Prometheus
├── grafana/               # Provisioning Grafana (datasources, dashboards)
├── requirements.txt       # Dépendances Python
├── save_model.py          # Chargement du modèle
├── templates/             # Interface utilisateur HTML
├── images/                # Images explicatives (schéma, captures)
└── dataset_organisé/      # Jeux de données structurés

🚀 Installation et exécution

Cloner le dépôt

git clone <url-du-repo>
cd Pathologies-Dentaires

Construire et lancer les services

docker-compose up --build

Arrêter les services

docker-compose down

🔓 Accès aux services

Application Web : http://localhost:5000 — Interface de classification

Prometheus : http://localhost:9090 — Métriques collectées

Grafana : http://localhost:3000 (admin/admin) — Tableaux de bord

🏢 Architecture du projet

L’architecture repose sur plusieurs conteneurs Docker :

Flask App : Service principal de classification

Prometheus : Collecte des métriques exposées par Flask

Grafana : Visualisation des tableaux de bord

![Schéma de l'architecture](images/shema.png)


📊 Supervision et métriques

L’application expose des métriques via Prometheus, visibles dans Grafana :

Métriques système :

Utilisation CPU

Mémoire

Activité réseau

Métriques applicatives :

Nombre de prédictions par classe

Latence des prédictions

Détails des requêtes HTTP



🔹 Interface utilisateur

Permet de téléverser une image dentaire et d’obtenir une classification automatique.

![Interface de l'application](images/app.png)


🌐 Informations sur les maladies

Détails sur les pathologies détectées par le modèle :

![Informations maladies](images/info.png)


⚙️ Personnalisation & Extension

Ajout de pathologies : Ajoutez des images dans dataset_organisé/ et réentraînez le modèle

Dashboards Grafana : Modifiez-les dans grafana/provisioning/dashboards/

Ajout de métriques : Instrumentez app_modified.py pour plus de métriques


📈 Visualisation des métriques

Les métriques collectées sont visualisées dans Grafana :

![Visualisation Grafana](images/Grafana.png)


📚 Auteurs

Projet réalisé par [Votre Nom] dans le cadre de [Projet universitaire / Stage].

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

