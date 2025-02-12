import string

from random import choice
from client import Client
from client import get_name, get_lastname
from client import get_gender, get_height
from client import get_weight, get_age, get_activite_level

def initial_screen():
    welcome_greeting = '\nWelcome to the Personal Trainer Tool\n'
    print(welcome_greeting.upper())
    print('Made for user by Personal Trainer Professional\n')
    print('To use this app, hit enter after each choice.\n')

    while True:
        nclient_or_eclient = input(
            'Hit "N" to add new client or "E" for existing client:\n\n'
        )
        nclient_or_eclient = nclient_or_eclient.lower()
        if  nclient_or_eclient == 'n':
            new_client()
            return False 

        if nclient_or_eclient == 'e':
            return False
        
        print('\nInvalid entry, please try again\n')

def new_client():
    print('\nLets add a new client...\n')
    print('Client data will be saved to our database upon confirmation.\n\n')
    new_or_back = input(
        'Hit "1" to continue or any other key to go back.\n\n'
        )
    if new_or_back == "1":
        process_client_details()
    else:
        initial_screen()


def process_client_details():
    print("Let's get client personal data...\n")
    new_client = Client(get_name(), get_lastname(), get_gender(), get_height(), get_weight(), get_age(), get_activite_level())
    print("\n\nProcessing New Client data...\n\n ")
    print(new_client.description())
   # next()

    #inserindo valores informados do Cliente em variáveis separadas para facilitar interação
    name = new_client.name
    lastname = new_client.last_name
    gender = new_client.gender
    height = new_client.height
    weight = new_client.weight
    age = new_client.age
    act_level = float(new_client.act_level)

    #chama a função create_id e informa ao novo Cliente
    id = int(create_id())

    #calcule o IMC chamando sua função e passe para o novo cliente.
    bmi = check_bmi(name, weight, height)
    #next()   

    #calcule o BMR chamando sua função e passe para o novo cliente.
    bmr = check_bmr(name, gender, weight, height, age)
    #next()

    #Calcule a dieta chamando sua função e exiba o resultado final
    diet_process = create_diet(name, bmr, act_level)
    loss = int(diet_process * 0.85) #menos 15% KCAL por dia para perder peso
    mantain = int(diet_process)
    gain = int(diet_process * 1.15) #mais 15% KCAL por dia para ganhar peso 

    print(f"For WEIGHT LOSS it's recommended: {loss} KCAL daily.")
    print(f"For MANTAIN WEIGHT it's recommended: {mantain} KCAL daily.")
    print(f"For WEIGHT GAIN it's recommended: {gain} KCAL daily.")

    

#função para criar um id único para cada cliente com 6 digitos
def create_id():
    chars = string.digits
    random = ''.join(choice(chars) for _ in range(6))
    id = random
    return id

#função para calcular o IMC do cliente
def check_bmi(name, weight, height):
    print("-------------------------\n")
    print("Let's calculate their (BMI)")
    print("BMI (body mass index) is a measure of whether")
    print("you're a healthy weight for your height\n")

    #Calcule o IMC e mostre para o usuário
    bmi_check = weight / (height/100)**2
    bmi = round(bmi_check,1)
    print(f"{name} BMI is: {bmi}\n")

    #Condição para verificar se o cliente está saudável ou não pelo IMC
    if bmi <= 18.4:
        print(f"{name} is underweight.\n")
    elif bmi <= 24.9:
        print(f"{name} is healthy.\n")
    elif bmi <= 29.9:
        print(f"{name} is over weight.\n")
    elif bmi <= 34.9:
        print(f"{name} is severely over weight.\n")
    elif bmi <= 39.9:
        print(f"{name} is obese.\n")
    else:
        print(f"{name} is severely obese.\n")
    return bmi

#função para calcular o BMR do cliente (Taxa metabólica basal)
def check_bmr(name, gender, weight, height, age):
    print("Let's calculate their (BMR)")
    print("BMR (Basal metabolic rate) is the amount of")
    print("energy expended per day at rest.")
    print("This is fundamental to decide either if it is needed to consume")
    print("more or less KCAL per day, depending on the client objective\n")

    if gender == "m":
        brm = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    print(f"{name} BMR is: {bmr}\n")
    return bmr


def create_diet (name, bmr, act_level):
    #Função para calcular o consumo real de KCAL do cliente, dependendo do nível de atividade
    print("-------------------------\n")
    print("Let's create a daily KCAL diet")   

    if act_level == 1:
        real_bmr = bmr * 1.2
    elif act_level == 2:
        real_bmr = bmr * 1.375
    elif act_level == 3:
        real_bmr = bmr * 1.55
    elif act_level == 4:
        real_bmr = bmr * 1.725
    else:
        real_bmr = bmr * 1.9

    print (f"Prossesing {name} diet...\n\n")
    return real_bmr






    
initial_screen()