# Analyse IP
# Calcul moyenne
# Detection des IP > 10 * moyenne


# Detecter les volumes importants de requêtes suspectes (quantil)
# Distribuer les IP par nombre de requetes (5% les plus élevés)

import csv
from pathlib import Path

log_path= Path(__file__).resolve().parent / 'logs.csv'
# Chemin vers votre fichier CSV
# fichier_csv = 'D:\Info\Dev\data\data_python_lesson\data_lesson\exercices\02. data_analyse\log_analysis\script.py'
# Création d'un dictionnaire pour compter les occurrences des adresses IP
ip_counts = {}
ip_avg ={}
# Ouvrir le fichier CSV
with open(log_path, mode='r', encoding='utf-8') as fichier:
    lecteur_csv = csv.DictReader(fichier)
    # datas = list(lecteur_csv)
    # Passer l'en-tête si nécessaire
    next(lecteur_csv)
    
    # Lire les lignes du fichier CSV
    for ligne in lecteur_csv:
        ip = ligne["source_ip"]
        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1
    total = 0
    for value in ip_counts.values():
        total += value
    
    avg = total/len(ip_counts)
    ten_avg = avg * 10

    for key,value in ip_counts.items():
        if value > ten_avg:
            print(key,value)
    # print(ip_avg)

# Affichage du dictionnaire des comptes d'adresses IP
# print(ip_counts)

        # print(ligne)  # 'ligne' est une liste contenant les valeurs des cellules de la ligne courante

