import string

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
    new_client = Client(get_name(), get_lastname(), get_gender(), get_height(), get_weight(), get_age(), get_activite_level)
    print("\n\nProcessing New Client data...\n\n ")
    print(new_client.description())
   # next()

    #criando variáveis separadas para facilitar interação 
    name = new_client.name
    lastname = new_client.last_name
    gender = new_client.gender
    height = new_client.height
    weight = new_client.weight
    age = new_client.age
    act_level = float(new_client.act_level)


    


initial_screen()