import os
import io
import torch
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from flask import Flask, render_template, request, jsonify
from save_model import load_model
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Métriques personnalisées sont définies directement dans les décorateurs de route

# Définir les classes de pathologies dentaires
CLASSES = ['Calculus', 'Caries', 'Gingivitis', 'Hypodontia', 'Tooth Discoloration', 'Ulcers']

# Charger le modèle
model_path = 'models/dental_pathology_model.pth'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = load_model(model_path, num_classes=6, device=device)

# Définir les transformations pour les images
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])

def predict_image(image):
    """Prédit la pathologie dentaire à partir d'une image"""
    # Prétraiter l'image
    image = transform(image).unsqueeze(0).to(device)
    
    # Désactiver le calcul du gradient pour l'inférence
    with torch.no_grad():
        outputs = model(image)
        # Obtenir les probabilités avec softmax
        probs = torch.nn.functional.softmax(outputs, dim=1)[0]
        # Obtenir la classe prédite
        _, predicted = torch.max(outputs, 1)
    
    # Convertir en valeurs Python
    probs = probs.cpu().numpy()
    predicted_class = predicted.item()
    
    # Créer un dictionnaire avec les probabilités pour chaque classe
    results = {
        'class': CLASSES[predicted_class],
        'confidence': float(probs[predicted_class]),
        'probabilities': {CLASSES[i]: float(probs[i]) for i in range(len(CLASSES))}
    }
    
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
@metrics.summary('dental_prediction_latency_seconds', 'Time spent processing prediction')
@metrics.counter('dental_prediction_count', 'Number of predictions')
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucune image n\'a été téléchargée'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'})
    
    try:
        # Lire l'image
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
        
        # Faire la prédiction
        results = predict_image(img)
        
        # Le compteur est automatiquement incrémenté par le décorateur
        
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

# Ajouter une route pour vérifier la santé de l'application
@app.route('/health')
@metrics.do_not_track()
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)