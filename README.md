🦷 Classification des Pathologies Dentaires avec Supervision via Docker, Prometheus et Grafana
Ce projet propose une application web intelligente pour la classification automatique des pathologies dentaires à partir d'images, enrichie par une supervision complète des métriques système et applicatives à l’aide de Prometheus et Grafana. Le tout est orchestré via Docker Compose pour une installation et une gestion simplifiées.

🔧 Technologies Utilisées:

🐍 Python, Flask : Backend de l'application web

🔥 PyTorch : Modèle de classification dentaire

📈 Prometheus : Collecte de métriques

📊 Grafana : Visualisation des métriques

🐳 Docker & Docker Compose : Conteneurisation et orchestration

🎨 HTML/CSS : Interface utilisateur

⚡ Prérequis:

Docker

Docker Compose

📁 Structure du Projet
bash
Copier
Modifier
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

🚀 Installation & Exécution

Cloner le dépôt

bash
Copier
Modifier
git clone <url-du-repo>
cd Pathologies-Dentaires
Construire et lancer les services

bash
Copier
Modifier
docker-compose up --build
Arrêter les services

bash
Copier
Modifier
docker-compose down
🌐 Accès aux Services
Service	URL	Description
🖥️ Application	http://localhost:5000	Interface de classification d’images
📡 Prometheus	http://localhost:9090	Consultation des métriques collectées
📊 Grafana	http://localhost:3000	Tableaux de bord (admin/admin)

🏗️ Architecture du Projet:

L’architecture repose sur une stack multi-conteneurs Docker :

Flask App : Service principal de classification

Prometheus : Collecte des métriques exposées par Flask

Grafana : Visualisation des métriques



📊 Supervision et Métriques:

L’application expose des métriques détaillées :

🔧 Métriques système :
Utilisation CPU

Utilisation de la mémoire

Activité réseau

🧠 Métriques applicatives :
Nombre de prédictions par classe

Temps de réponse moyen

Nombre et statut des requêtes HTTP

➡️ Ces métriques sont collectées automatiquement via Prometheus et visualisées dans Grafana :
![Visualisation Grafana](images/Grafana.png)



🧑‍💻 Interface Utilisateur
Permet de téléverser une image dentaire et d’obtenir une classification instantanée :
![Interface de l'application](images/app.png)



🦷 Informations sur les Pathologies
Un aperçu des pathologies détectées par le modèle :![Informations maladies](images/info.png)



⚙️ Personnalisation & Extension
🔁 Ajout de pathologies : Ajouter des images dans dataset_organisé/ et réentraîner le modèle.

📐 Dashboards Grafana : Modifier ceux existants dans grafana/provisioning/dashboards/.

📥 Ajout de métriques personnalisées : Modifier app_modified.py pour ajouter des @summary, @counter, etc.

👨‍🔧 Auteurs
Projet réalisé par Aghzar Otmane dans le cadre de projet universitaire
