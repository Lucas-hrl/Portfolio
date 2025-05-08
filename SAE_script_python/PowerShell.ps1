# Spécifier le chemin vers l'interpréteur Python
$pythonPath = "C:/Users/RockylucM160/Desktop/Sae_105-Traiter_les_donnees/.venv/Scripts/python.exe"  # Remplacez par le chemin de votre installation Python

# Chemin du script Python à exécuter
$pythonScript = "C:\Users\RockylucM160\Desktop\Sae_105-Traiter_les_donnees\SAE_script_python\Script2.py"
$affichageScript = "C:\Users\RockylucM160\Desktop\Sae_105-Traiter_les_donnees\SAE_script_python\Script3.py"
# Exécute le script Python qui ouvre le sélecteur et récupère le répertoire sélectionné
$repertoire_de_base = & $pythonPath C:\Users\RockylucM160\Desktop\Sae_105-Traiter_les_donnees\SAE_script_python\Script1.py

# Vérifie si un répertoire a été sélectionné
if (-not $repertoire_de_base) {
    Write-Host "Aucun repertoire selectionne. Le script est annule."
    exit 1
}

# Vérifie si le répertoire sélectionné est valide
if (Test-Path $repertoire_de_base) {
    Write-Host "Repertoire valide : $repertoire_de_base"
    # Exécuter le script Python avec repertoire_de_base comme argument
    & $pythonPath $pythonScript "$repertoire_de_base"
} else {
    Write-Host "Le repertoire selectionne n'existe pas ou est invalide."
    exit 1
}
# Chemin du fichier JSON généré par Script2.py
$jsonFile = "C:\Users\RockylucM160\Desktop\Sae_105-Traiter_les_donnees\SAE_script_python\gros_fichiers.json"
& $pythonPath $affichageScript "$jsonFile"


