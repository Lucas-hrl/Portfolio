# Chemin du dossier contenant ce script PowerShell
$projectRoot = $PSScriptRoot

# Chemins des scripts et du JSON (pas de doublon de dossier ici)
$pythonPath = Join-Path $projectRoot ".venv\Scripts\python.exe"
$script1 = Join-Path $projectRoot "Script1.py"
$script2 = Join-Path $projectRoot "Script2.py"
$script3 = Join-Path $projectRoot "Script3.py"
$jsonFile = Join-Path $projectRoot "gros_fichiers.json"


# Lancer le script Python qui ouvre le sélecteur et récupère le répertoire sélectionné
$repertoire_de_base = & $pythonPath $script1

# Vérifier si un répertoire a été sélectionné
if (-not $repertoire_de_base) {
    Write-Host "Aucun répertoire sélectionné. Le script est annulé."
    exit 1
}

# Vérifier si le répertoire est valide
if (Test-Path $repertoire_de_base) {
    Write-Host "Répertoire valide : $repertoire_de_base"
    # Lancer Script2.py avec le répertoire en paramètre
    & $pythonPath $script2 "$repertoire_de_base"
    # Lancer Script3.py avec le JSON en paramètre
    & $pythonPath $script3 "$jsonFile"
} else {
    Write-Host "Le répertoire sélectionné n'existe pas ou est invalide."
    exit 1
}
