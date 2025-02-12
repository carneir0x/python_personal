#classe usada para representar um Cliente
class Client:
    def __init__(self, name, last_name, gender, height, weight, age, act_level):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.act_level = act_level

    #descreve a instância do novo Cliente
    def description(self):
        print(f"Name: {self.name}, Last Name: {self.last_name}, Gender: {self.gender}, Height: {self.height}, Weight: {self.weight}, Age: {self.age}, Activite Level: {self.act_level}")
        return "\n\nClient succesfully created!\n"

#função para obter a entrada do nome e validar
def get_name():
    while True:
        name = input('Client name? \n\n').lower()
        if name.isalpha():
            return name
        print('\nInvalid input! All characters should be alphabet letters')

#função para obter o sobrenome e validar
def get_lastname():
    while True:
        lastname = input("Client last name? \n\n").lower()
        if lastname.isalpha():
            return lastname
        print('\nInvalid input! All characters should be alphabet letters')

#função para obter o gênero e validar
def get_gender():
    while True:
        gender = input("Client gender? Hit F for female or M for male.\n")
        if gender == "f":
            return gender
        if gender == "m":
            return gender
        else: 
            print("Invalid input!")

#função para obter a altura e validar
def get_height():
    while True:
        height = input("Client height (CM)? It MUST be in Centimeters!!\n\n")
        if height.isnumeric():
            return int(height)
        print("\nInvalid input! All characters should be numbers (1-10)")

#função para obter o peso e validar
def get_weight():
    while True:
        weight = input("Client weight (kg) ? It MUST be in Kilogram!!\n\n")
        if weight.isnumeric():
            return int(weight)

#função para obter a idade e validar
def get_age():
    while True:
        age = input("Client age? \n\n")
        if age.isnumeric():
            return int(age)
        print("\nInvalid input! All characters should be numbers (1-10)")

#função para obter a entrada no nível de atividade e validar
def get_activite_level():
    print("Client Activite Level? Digit one of the following options:\n")
    print("'1' for sedentary (little or no exercise)")
    print("'2' for lightly active (light exercise 1-3 days/week)")
    print("'3' for moderately active (moderate exercise 3-5 days/week")
    print("'4' for very active (hard exercise/sports 6-7 days a week)")
    print("'5' for extra active (very hard exercise/sports & physical job)")
    while True:
        activite = input()

        if activite == "1":
            return float(activite)
        elif activite == "2":
            return float(activite)
        elif activite == "3":
            return float(activite)
        elif activite == "4":
            return float(activite)
        elif activite == "5":
            return float(activite)
        else:
            print("Invalid input!")


    

                
