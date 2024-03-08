temperatures = [
    [15, 14, 14, 13, 13, 14, 15, 16, 18, 20, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14],
    [14, 13, 13, 12, 12, 13, 14, 16, 18, 21, 23, 24, 25, 25, 24, 23, 22, 21, 19, 18, 17, 15, 14, 13],
    [13, 12, 12, 11, 11, 12, 13, 15, 17, 20, 22, 23, 24, 24, 23, 22, 21, 20, 18, 17, 16, 14, 13, 12],
    [14, 13, 13, 12, 12, 14, 15, 17, 19, 22, 24, 25, 26, 26, 25, 24, 23, 22, 20, 19, 18, 16, 15, 14],
    [15, 14, 14, 13, 13, 15, 16, 18, 20, 23, 25, 26, 27, 27, 26, 25, 24, 23, 21, 20, 19, 17, 16, 15],
    [16, 15, 15, 14, 14, 16, 17, 19, 21, 24, 26, 27, 28, 28, 27, 26, 25, 24, 22, 21, 20, 18, 17, 16],
    [15, 14, 14, 13, 12, 14, 15, 17, 19, 22, 24, 25, 26, 26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 15]
]

# Quelle est la température à midi le mercredi ?

jours_lib = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
jour_i = 2
heure_i = 12
print(f"Température à {heure_i}h, le {jours_lib[jour_i]}:", temperatures[jour_i][heure_i], "°C")

# Afficher toutes les températures (essayer de rendre la sortie propre)

for jour in range(7):
    print(jours_lib[jour], ":")
    for heure in range(24):
        print(f"{heure}h: {temperatures[jour][heure]}°C", end=" | ")
    print("\n")

# Créer une fonction qui calcule la moyenne sur une journée
    
def moyenne_jour(temp, day):
    total_temperature = sum(temp[jour])
    nombre_heures = len(temp[jour])
    temp_moy = total_temperature / nombre_heures

    print(f"Temp moy: {temp_moy:.2f}°C")

moyenne_jour(temperatures, 2)

temp = [
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ],
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ],
]