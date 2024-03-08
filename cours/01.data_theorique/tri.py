import random
import timeit
import asyncio
import random

# association = False

# def afficher_association(assoc):
#     # if assoc:
#     #     return "Oui"
#     # else:
#     #     return "Non"
#     return "Oui" if assoc else "Non"

# print(afficher_association(association))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def generate_random_list(size):
    return [random.randint(0, 9999) for _ in range(size)]

# sizes = [100, 1000, 10000]
sizes = [1000]

for size in sizes:
    arr = generate_random_list(size)
    arr_bubble = arr.copy()
    arr_sorted = arr.copy()

    timeit_bubble = timeit.timeit('bubble_sort(arr_bubble)', globals=globals(), number=1)

    timeit_sorted = timeit.timeit('sorted(arr_sorted)', globals=globals(), number=1)

    print(f"Tri à bulles pour {size} éléments: {timeit_bubble:.6f} secondes")
    print(f"Tri sorted de Python pour {size} éléments: {timeit_sorted:.6f} secondes")

async def sort_val(val):
    await asyncio.sleep(val)
    print(val, end=" ",flush=True)

async def sleep_sort(values):
    tasks = [sort_val(val) for val in values]
    await asyncio.gather(*tasks)

lst = [3, 1, 10]
print("Début du tri",lst)

asyncio.run(sleep_sort(lst))
print("Fin du tri")

def pizza(*ingredients):
    print(ingredients)