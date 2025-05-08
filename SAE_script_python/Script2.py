
from pathlib import Path
import json
import sys  #module est utilisé pour récupérer les arguments de ligne de commande

def lister_fichiers_et_tailles(repertoire_de_base):
    fichiers_info = []
    info = []
    # Parcours récursif de tous les fichiers dans le répertoire de base et ses sous-répertoires
    for fichier in Path(repertoire_de_base).rglob('*'):  # rglob('*') parcourt tous les fichiers récursivement
        if fichier.is_file():  # Vérifie que c'est bien un fichier
            chemin = fichier.resolve() #chemin absolu du fichier de type Path
            taille = fichier.stat().st_size #taille en octets du fichier
            info.append(chemin)
            info.append(taille)
            fichiers_info.append(info)
            info = []
    return fichiers_info

def tri_decroissant (liste):
    return sorted(liste, key=lambda x: x[1], reverse=True)

def choix_fichier(liste_decroissante,TAILLE_MINI_FICHIER_EN_MEGA_OCTET,NB_MAXI_FICHIERS):
    taille_min_octets = TAILLE_MINI_FICHIER_EN_MEGA_OCTET * 1024 * 1024
    fichier_filtre = []
    for i in liste_decroissante:
        if i[1]> taille_min_octets and len(fichier_filtre) < NB_MAXI_FICHIERS:
            fichier_filtre.append(i)
    return fichier_filtre

def fich_json(liste_fichier, nom_fichier):
    lst_json=[]
    for fich in liste_fichier:
        t=str(fich[0]).replace('\\', '\\\\')
        lst_json.append([t, fich[1]])  # Ajoute une liste avec t et le deuxième élément de fich

    with open(nom_fichier, mode='w', encoding='utf-8') as json_file:
        json.dump(lst_json, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:  #vérifie que le nombre d'arguments passés en par pwsh est bien égal à 2 (le script et le répertoire de base)
        print("Usage : python Script2.py <repertoire_de_base>")
        sys.exit(1)

    rep = sys.argv[1]  # Récupération du rep_de_base depuis pwsh

liste = lister_fichiers_et_tailles(rep)
liste_triee= tri_decroissant(liste)
liste_filtre= choix_fichier(liste_triee,10 ,100)
#for nom_fich, taille in liste_filtre:
 #   print(f"{nom_fich} - Taille : {taille} octets")

fich_json(liste_filtre,'gros_fichiers.json')

