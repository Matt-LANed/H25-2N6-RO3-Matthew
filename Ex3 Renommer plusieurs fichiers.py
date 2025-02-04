# importez os
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
import os
chemin = os.environ.get("USERPROFILE")
os.chdir(f"{chemin}/Downloads/R03 Exercices Depart/Ex3 Videos")
file = f"{chemin}/Downloads/R03 Exercices Depart/Ex3 Videos"

print(os.getcwd())

for dossier in os.listdir():
    
    nom = os.path.splitext(f"{chemin}/{dossier}")
    filename = nom[0]
    ext = nom[1]
    liste = filename.split("_")
    num = liste[2]
    real_num = num.replace("#", "")
    name = liste[0]
    liste_stripped = name.strip()
    if len(real_num) == 1:
        real_num.zfill(2)
    os.rename(f"{file}{dossier}", f"{liste_stripped}#{real_num}{ext}")

#Rien fonctionne, quelle souffrance
