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
        print("vc digitou 1")
        #  process_client_details()
    else:
        initial_screen()

    


initial_screen()