import os
import torch
import torch.nn as nn
from torchvision.models import densenet121

# Définition de la classe CustomDenseNet comme dans le notebook
class CustomDenseNet(nn.Module):
    def __init__(self, num_classes=6):
        super(CustomDenseNet, self).__init__()
        self.model = densenet121(weights=True)  # Charger le modèle pré-entraîné DenseNet121
        self.model.classifier = nn.Linear(self.model.classifier.in_features, num_classes)
        
    def forward(self, x):
        return self.model(x)

def save_model(model, save_path='dental_pathology_model.pth'):
    """
    Sauvegarde le modèle entraîné dans un fichier
    
    Args:
        model: Le modèle PyTorch à sauvegarder
        save_path: Chemin où sauvegarder le modèle
    """
    # Créer le dossier models s'il n'existe pas
    os.makedirs(os.path.dirname(save_path) if os.path.dirname(save_path) else '.', exist_ok=True)
    
    # Sauvegarder le modèle
    torch.save(model.state_dict(), save_path)
    print(f"Modèle sauvegardé avec succès à {save_path}")

def load_model(model_path='dental_pathology_model.pth', num_classes=6, device='cpu'):
    """
    Charge un modèle sauvegardé
    
    Args:
        model_path: Chemin vers le fichier du modèle sauvegardé
        num_classes: Nombre de classes pour le modèle
        device: Appareil sur lequel charger le modèle ('cpu' ou 'cuda')
        
    Returns:
        Le modèle chargé
    """
    # Initialiser le modèle
    model = CustomDenseNet(num_classes=num_classes)
    
    # Charger les poids du modèle
    model.load_state_dict(torch.load(model_path, map_location=device))
    
    # Mettre le modèle en mode évaluation
    model.eval()
    
    print(f"Modèle chargé avec succès depuis {model_path}")
    return model

if __name__ == "__main__":
    # Exemple d'utilisation pour sauvegarder un modèle
    # Créer une instance du modèle
    model = CustomDenseNet(num_classes=6)  # 6 classes: Caries, Tartre, Gingivite, Ulcères, Décoloration, Hypodontie
    
    # Définir le chemin de sauvegarde
    model_save_path = "models/dental_pathology_model.pth"
    
    # Sauvegarder le modèle
    save_model(model, model_save_path)
    
    # Exemple de chargement du modèle
    loaded_model = load_model(model_save_path)
    print("Modèle prêt pour les prédictions!")