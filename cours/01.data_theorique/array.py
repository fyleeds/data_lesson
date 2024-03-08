#    array 2D

#       1
#       |
#       |
#       v
#           2 --->

tableau_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(tableau_2d[1][2])

import array

taille = 3
tableau_1d = array.array('i', [0] * (taille * taille))
print(tableau_1d)

def get_index(x, y, dimension):
    return x * y + dimension

tableau_1d[get_index(1, 1, taille)] = 99

print(tableau_1d)