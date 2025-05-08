import json
import os
import random
import sys  #module est utilisé pour récupérer les arguments de ligne de commande
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer
from Creation_Onglets import Onglets
from Creation_Camembert import Camembert
from Creation_Legendes import Legendes
from Creation_Boutons import Boutons


import json

def recup_json(nom_fichier):
    with open(nom_fichier, mode='r', encoding='utf-8') as file:
        fichier = json.load(file)  #fichier contient donc une liste de liste
    return sorted(fichier, key=lambda x: x[1], reverse=True) #tri décroissant de fichier par taille


def generer_couleurs_aleatoires(NB_MAXI_FICHIERS):
    liste_couleurs = []
    for i in range(NB_MAXI_FICHIERS):
        r = random.randint(0, 255)  # Valeur rouge aléatoire
        g = random.randint(0, 255)  # Valeur verte aléatoire
        b = random.randint(0, 255)  # Valeur bleue aléatoire
        couleur = QColor(r, g, b)  # Création d'un objet QColor
        liste_couleurs.append(couleur)
    return liste_couleurs

def normaliser_chemin_fichier(chemin):
    return os.path.normpath(chemin)  # Normalisation multiplateforme


def creation_script_suppression(liste_legende):
    if not liste_legende:
        QMessageBox.critical(None, "Erreur", "Aucune légende trouvée. Impossible de générer le script.")
        return

    script_contenu = [
        'Write-Output "Script PowerShell pour supprimer des fichiers sans confirmation"',
        'Write-Output "Attention : cette suppression est définitive ..."',
        '$reponse = Read-Host "Veuillez confirmer la suppression de tous ces fichiers : (OUI)"',
        'if ($reponse -eq "OUI") {',
        '    $confirmation = Read-Host "Êtes-vous bien certain(e) ? (OUI)"',
        '    if ($confirmation -eq "OUI") {'
    ]

    fichiers_a_supprimer = []  # Stocke les fichiers à supprimer

    for page_legende in liste_legende:
        etats_cases = page_legende.recupere_etats_cases_a_cocher()
        fichiers_page = page_legende.liste_fichiers  # Liste des fichiers pour cette page

        if etats_cases is None:
            QMessageBox.critical(None, "Erreur", "Impossible de récupérer les états des cases à cocher.")
            return

        # Associer chaque fichier à son état (True = à supprimer)
        for i in range(len(etats_cases)):
            if etats_cases[i]:  # Si la case est cochée
                chemin_fichier = normaliser_chemin_fichier(fichiers_page[i][0])
                fichiers_a_supprimer.append(f'        Remove-Item -Path "{chemin_fichier}" -Force')

    if not fichiers_a_supprimer:
        QMessageBox.information(None, "Aucun fichier sélectionné", "Aucun fichier à supprimer.")
        return

    # Ajouter les suppressions de fichiers dans le script
    script_contenu.extend(fichiers_a_supprimer)

    # Ajouter la fin du script PowerShell
    script_contenu.extend([
        '    } else {',
        '        Write-Output "Opération annulée..."',
        '    }',
        '} else {',
        '    Write-Output "Opération annulée..."',
        '}'
    ])

    # Sauvegarde du script PowerShell dans un fichier
    with open("delete_files.ps1", "w", encoding="utf-8") as script_file:
        script_file.write("\n".join(script_contenu))

    QMessageBox.information(None, "Succès", "Le script PowerShell a été généré avec succès.")


if __name__ == "__main__":
    NB_LEGENDES_PAR_PAGE = 25
    repertoire_base = "gros_fichiers.json"

    # Lecture du fichier JSON
    liste_fichiers = recup_json(repertoire_base)
    NB_MAXI_FICHIERS = len(liste_fichiers)

    # Génération des couleurs aléatoires
    liste_couleurs = generer_couleurs_aleatoires(NB_MAXI_FICHIERS)

    appli = QApplication(sys.argv)  #Création de l’environnement graphique « PyQt »
    fenetre = Onglets() #Création du conteneur d’onglets

    # Ajout du camembert
    fromage = Camembert(liste_fichiers, liste_couleurs)
    layout_fromage = fromage.dessine_camembert()
    fenetre.add_onglet("Camembert", layout_fromage)

    # Ajout des légendes (1 à 4 onglets selon le nombre de fichiers)
    liste_legendes = []
    for num_page in range((NB_MAXI_FICHIERS // NB_LEGENDES_PAR_PAGE) + 1):
        legende = Legendes(liste_fichiers, liste_couleurs, NB_LEGENDES_PAR_PAGE * num_page, NB_LEGENDES_PAR_PAGE)
        layout_legende = legende.dessine_legendes()
        liste_legendes.append(legende)
        fenetre.add_onglet(f"Légende {num_page + 1}", layout_legende)

    # Ajout de l'onglet contenant les boutons
    ihm = Boutons(repertoire_base, lambda: creation_script_suppression(liste_legendes)) #lambda permet que la fonction soit appelé seulement au clic du bouton
    layout_ihm = ihm.dessine_boutons()
    fenetre.add_onglet("IHM", layout_ihm)

    # Affichage de la fenêtre principale
    fenetre.show()
    sys.exit(appli.exec_())




