import random

database = {}

def init():
    print('Welcome to Bank Cece')

    haveAccount = int(input('Do you have an account with us: 1 (Yes) 2 (No) \n'))
    
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        init ()

def login():
    print('Login into your account')

    accountNumberFromUser = int(input('What is your account number \n'))
    password = input('What is your password \n')

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()
             
def register():
    print('**** Register ****')

    email = input('What is your email address \n')
    name = input('What is your first name? \n')
    lName = input('What is your last name? \n')
    password = input('Create a Password \n')

    accountNumber = generationAcctNumber()

    database[accountNumber] = [ name, lName, email, password ]

    print('Your account has been created')
    print('------ ------ ------')
    print('Your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print('------ ------ ------')


    login ()

def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))
    
    selectedOption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption ==2):
        withdrawalOperation()
    elif(selectedOption ==3):
        logout()
    elif(selectedOption ==4):
        exit()
    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    remainingBalance = balanceNumber() 
    withdrawalOption = int(input('How much would you like to withdrawal? \n'))
    if(withdrawalOption >= 0):
        print('Take your money')
        print('Remaining Balance is %d' % remainingBalance)
        init ()
  
def balanceNumber():
    return random.randrange(111111, 999999)


def depositOperation():
    accountBalance = balanceNumber()
    print('Insert Deposit')
    print('Account balance is now %d' % accountBalance)
    init ()

def generationAcctNumber():

    return random.randrange(1111111111, 9999999999)

def logout():
    login()

init()



