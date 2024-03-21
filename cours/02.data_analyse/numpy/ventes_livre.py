# Générer une série (1d) qui représente un nimbre aléatore de vente de livre entre 50 et 100 ventes sur la semaine passée
#prix entre 7 et 35
#toujoues par 0 ou 50 centimes
# Calculer la moyenne et mediane des ventes
# Calculer l'ecart type des ventes

import numpy as np


# Définir les limites en euros
min_euro, max_euro = 7, 35

# Générer un tableau pour chaque euro dans la plage spécifiée
euros = np.arange(min_euro, max_euro +0.5 ,0.5)

ventes = np.random.choice(euros, size= np.random.randint(50, 100))
print(ventes)

print(np.mean(ventes).round(2))  
print(np.median(ventes).round(2))
print(np.std(ventes).round(2))

