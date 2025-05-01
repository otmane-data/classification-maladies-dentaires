# Script pour vérifier l'installation des bibliothèques nécessaires

def check_libraries():
    libraries = {
        'os': 'Module intégré',
        'shutil': 'Module intégré',
        'random': 'Module intégré',
        'numpy': 'Pour le traitement numérique',
        'matplotlib': 'Pour la visualisation',
        'seaborn': 'Pour des visualisations statistiques avancées',
        'PIL': 'Pour le traitement d\'images',
        'sklearn': 'Pour l\'apprentissage automatique',
        'torch': 'Pour le deep learning',
        'torchvision': 'Pour le traitement d\'images avec PyTorch'
    }
    
    missing = []
    installed = []
    
    for lib, description in libraries.items():
        try:
            if lib == 'PIL':
                # PIL est importé comme Image
                from PIL import Image
                installed.append(f'{lib}: {description}')
            else:
                __import__(lib)
                installed.append(f'{lib}: {description}')
        except ImportError:
            missing.append(f'{lib}: {description}')
    
    print('\n===== BIBLIOTHÈQUES INSTALLÉES =====\n')
    for lib in installed:
        print(f'✓ {lib}')
    
    if missing:
        print('\n===== BIBLIOTHÈQUES MANQUANTES =====\n')
        for lib in missing:
            print(f'✗ {lib}')
        print('\nUtilisez la commande suivante pour installer les bibliothèques manquantes:')
        print(f"pip install {' '.join([lib.split(':')[0] for lib in missing if lib.split(':')[0] not in ['os', 'shutil', 'random']])}")
    else:
        print('\nToutes les bibliothèques nécessaires sont installées!')

if __name__ == '__main__':
    check_libraries()