from PyQt5.QtWidgets import QFileDialog, QApplication
import sys  #module est utilisé pour récupérer les arguments de ligne de commande

# Création de l'application PyQt (nécessaire pour QFileDialog)
app = QApplication(sys.argv)

# Ouverture du sélecteur de répertoire        None indique que la fenetre est independante, "Sele..." est le titre de la fenetre
repertoire = QFileDialog.getExistingDirectory(None, "Selectionner un repertoire")

# Affichage du chemin sélectionné uniquement
if repertoire:
    print(repertoire)  # Affiche uniquement le chemin pour une utilisation en PowerShell
else:
    print("")  # Retourne une chaîne vide si l'utilisateur annule

# Quitter l'application proprement
app.quit()
