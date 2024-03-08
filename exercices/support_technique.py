

# Fonction pour ajouter une demande de support
def ajouter_demande( client, demande):
    global file_attente
    obj = {'client': client, 'demande': demande}
    file_attente.append(obj)
    return file_attente
    # print("demande ajouté à fil d'attente : ",file_attente)
# Fonction pour traiter la première demande de support
def traiter_demande(file_attente):
    if file_attente:
        demande_traitee = file_attente.pop(0)
        print(f"Traitement de la demande de {demande_traitee['client']} : {demande_traitee['demande']}")
    else:
        print("La file d'attente est vide.")
    return file_attente

# Fonction pour afficher la file d'attente de support
def afficher_file_attente(file_attente):
    print("File d'attente de support :")
    i= 1
    for demande in file_attente:
        print(f"{i}  - {demande['client']} : {demande['demande']}")
        i += 1

# Initialiser la queue des demandes de support
file_attente = []
# Exemple de scénario
file_attente = ajouter_demande( "Alice", "Problème de connexion")
file_attente = ajouter_demande( "Bob", "Mot de passe oublié")
file_attente = ajouter_demande( "Charlie", "Problème de facturation")

file_attente = traiter_demande(file_attente)
file_attente = ajouter_demande( "Alice", "Question sur un produit")

afficher_file_attente(file_attente)
