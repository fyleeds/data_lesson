import random

def anniversaire_paradoxe(nb_personnes):
    anniversaires = [random.randint(1, 365) for _ in range(nb_personnes)]
    # print(anniversaires)
    anniversaires_uniques = len(set(anniversaires))
    return nb_personnes - anniversaires_uniques

nb_pers = 79
simulations = 10000

collision_count = sum(anniversaire_paradoxe(nb_pers) > 0 for _ in range(simulations))
print(f"Prob de collision: {(collision_count / simulations) * 100:.2f}%")