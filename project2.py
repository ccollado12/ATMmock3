import random
import validation
import database
import os
from getpass import getpass


def init():
    print('Welcome to Bank Cece')

    haveAccount = int(input('Do you have an account with us: 1 (Yes) 2 (No) \n'))

    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print('You have selected an invalid option')
        init()


def login():
    global accountNumberFromUser
    loginPath = 'data/auth_session/'
    print('***Login into your account***')

    accountNumberFromUser = input('What is your account number \n')
    f = open(loginPath + str(accountNumberFromUser) + '.txt', 'x')

    isAccountValid = validation.accountNumberValidation(accountNumberFromUser)

    if isAccountValid:

        password = getpass('What is your password? \n')

        user = database.authenticatedUser(accountNumberFromUser, password)
        if user:
            bankOperation(user)

        login()

    else:
        print('Account Number Invalid, must be 10 integers ')
        init()


def register():
    print('**** Register ****')

    email = input('What is your email address \n')
    name = input('What is your first name? \n')
    lName = input('What is your last name? \n')
    password = getpass('Create a Password \n')

    accountNumber = generationAcctNumber()
    # preparedUserDetails = name + ',' + lName + ',' + email + ',' + password + ',' + str(0)
    isUserCreated = database.create(accountNumber, name, lName, email, password)

    if isUserCreated:
        print('Your account has been created')
        print('------ ------ ------')
        print('Your account number is: %d' % accountNumber)
        print('Make sure you keep it safe')
        print('------ ------ ------')

        login()

    else:
        print('Something went wrong, please try again')
        register()


def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selectedOption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if selectedOption == 1:
        depositOperation()
    elif selectedOption == 2:
        withdrawalOperation(user)
    elif selectedOption == 3:
        logout()
    elif selectedOption == 4:
        exit()
    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation(user):
    currentBalance = int(user[4])
    withdrawalAmount = float(input('How much would you like to take out? \n'))

    if withdrawalAmount > currentBalance:
        return "Not sufficient funds/amount"
    else:
        print('Not sufficient funds/amount')

    newBalance = currentBalance - withdrawalAmount
    user[4] = newBalance
    updated_user = user[0] + ',' + user[1] + ',' + user[2] + ',' + user[3] + ',' + str(user[4])

    user_db_path = 'data/user_record/'
    f = open(user_db_path + str(accountNumberFromUser) + '.txt', 'w')
    f.write(updated_user)
    f.close()

    print("Withdrawal successful")
    if withdrawalAmount > 0:
        print('Your new balance is %s' % newBalance)
        otherOptions = int(input('Would you like to (1) Return to main menu (2) Log out \n'))

    if otherOptions == 1:
        init()
    elif otherOptions == 2:
        logout()
    else:
        withdrawalOperation(user)


def depositOperation(user):
    currentBalance = int(user[4])
    depositAmount = float(input('How much would you deposit? \n'))

    newBalance = currentBalance + depositAmount
    user[4] = newBalance
    updated_user = user[0] + ',' + user[1] + ',' + user[2] + ',' + user[3] + ',' + str(user[4])

    user_db_path = 'data/user_record/'
    f = open(user_db_path + str(accountNumberFromUser) + '.txt', 'w')
    f.write(updated_user)
    f.close()

    print("Deposit successful")

    if depositAmount > 0:
        print('Your new balance is %s' % newBalance)
        otherSelect = int(input('Would you like to (1) Return to main menu (2) Log out \n'))

    if otherSelect == 1:
        init()
    elif otherSelect == 2:
        logout()
    else:
        depositOperation(user)



def generationAcctNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    logoutPath = 'data/auth_session/'
    os.remove(logoutPath + str(accountNumberFromUser) + '.txt')

    login()


init()
