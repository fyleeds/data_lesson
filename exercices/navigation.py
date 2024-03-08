# pile -> stack
# file -> queue
# deque -> double-ended queue
    # LIFO (last in first out on peut surpprimer le premier élément)
    # push/pop


def valider_parenthese(chaine):
    stack = []
    for char in chaine:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0


print(valider_parenthese("(())"))

# Initialisation des stacks pour l'historique de navigation et les pages de retour
historique = []
pagesRetour = []

# Fonction pour visiter une nouvelle page
def visiter(url):
    global pagesRetour
    print(f"Visite : {url}")
    historique.append(url)
    pagesRetour = []  # This now correctly resets the global pagesRetour listcer l'historique de retour après avoir visité une nouvelle page

# Fonction pour retourner à la page précédente
def retour():
    if len(historique) > 1 : 
        pagesRetour.append(historique.pop())
        print(f"Retour à : {historique[-1]}")
    else:
        print("Aucune page précédente")


# Fonction pour avancer à la page suivante
def avant():
    if pagesRetour:
        page_suivante = pagesRetour.pop()
        historique.append(page_suivante)
        print(f"Avance à : {page_suivante}")

# Fonction pour afficher l'historique de navigation
def afficher_historique():
    print(f"  → Historique de navigation : {historique}")
    if pagesRetour:
        print(f"  → Pages disponibles pour un retour en avant : {pagesRetour}")
    else:
        print("  → Aucune page disponible pour un retour en avant")
    print(f"  → Pages disponibles pour un retour en arrières : {list(reversed(historique[:-1]))}")


# Exemple de scénario
visiter("page1.com")
visiter("page2.com")
visiter("page3.com")
afficher_historique()
retour()
retour()
afficher_historique()
visiter("page4.com")
afficher_historique()
