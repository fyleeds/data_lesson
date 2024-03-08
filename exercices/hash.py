pays = ["Afghanistan", "Afrique du Sud", "Allemagne", "Belgique", "Estonie"]

# Fonctions de hashage
    #Hashcode
# prendre une chaine et produire un nombre entier
#Fonction de compression
def hashcode(chaine):
    return sum([ord(char) for char in chaine])

    #Fonction de hachage
# une collision se fait quand deux chaines sont similaires apres le hashage
# Classe Student
    # Attributs
        # prenom
        # nom
        # date de naissance ("dd/mm/yyyy")
    #methode hash
        # le hashcode -> entier

class Student:
    def __init__(self, prenom, nom, date_de_naissance):
        self.prenom = prenom
        self.nom = nom
        self.date_de_naissance = date_de_naissance

    def __hash__(self):
        return hash((self.prenom, self.nom, self.date_de_naissance))
    
# Create some Student objects
student1 = Student("John", "Doe", "01/01/2000")
student2 = Student("Jane", "Doe", "02/02/2002")
student3 = Student("John", "Doe", "01/01/2000")  # Same as student1

# Print their hash values
print(hash(student1))
print(hash(student2))
print(hash(student3))

# Check if the hash of student1 and student3 are the same
print(hash(student1) == hash(student3))  # Should be True