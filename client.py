class Client:
    def __init__(self, name, last_name, gender, height, weight, age, act_level):
        self.name = name
        self.last_name = last_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.act_level = act_level

    def description(self):
        print(f"Name: {self.name}), Last Name: {self.last_name}, Gender: {self.gender,}, Height: {self.height}, Weight: {self.weight}, Age: {self.age}, Activite Level: {self.act_level}")
        return "\n\nClient succesfully created!\n"

def get_name():
    while True:
        name = input('Client name? \n\n').lower()
        if name.isalpha():
            return name
        print('\nInvalid input! All characters should be alphabet letters')

def get_lastname():
    while True:
        lastname = input("Client last name? \n\n").lower()
        if lastname.isalpha():
            return lastname
        print('\nInvalid input! All characters should be alphabet letters')

def get_gender():
    while True:
        gender = input("Client gender? Hit F for female or M for male.\n")
        if gender == "f":
            return gender
        if gender == "m":
            return gender
        else: 
            print("Invalid input!")

def get_height():
    while True:
        height = input("Client height (CM)? It MUST be in Centimeters!!\n\n")
        if height.isnumeric():
            return int(height)
        print("\nInvalid input! All characters should be numbers (1-10)")

def get_weight():
    while True:
        weight = input("Client weight (kg) ? It MUST be in Kilogram!!\n\n")
        if weight.isnumeric():
            return int(weight)

def get_age():
    while True:
        age = input("Client age? \n\n")
        if age.isnumeric():
            return int(age)
        print("\nInvalid input! All characters should be numbers (1-10)")

def get_activite_level():
    return int(1)


    

                
