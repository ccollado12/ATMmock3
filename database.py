import os
import database
import validation

user_db_path = 'data/user_record/'


def create(userAccountNumber, name, lName, email, password):
    userData = name + ',' + lName + ',' + email + ',' + password + ',' + str(0)

    if doesAccountNumberExist(userAccountNumber):
        return False
    if doesEmailExist(email):
        print('User already exists')
        return False

    completionState = False

    try:
        f = open(user_db_path + str(userAccountNumber) + '.txt', 'x')

    except FileExistsError:

        doesFileContainData = read(user_db_path + str(userAccountNumber) + '.txt')
        if not doesFileContainData:
            delete(userAccountNumber)

    else:
        f.write(str(userData))
        completionState = True
    finally:
        f.close()
        return completionState


def read(userAccountNumber):
    isAccountNumberValid = validation.accountNumberValidation(userAccountNumber)
    try:
        if isAccountNumberValid:
            f = open(user_db_path + str(userAccountNumber) + '.txt', 'r')
        else:
            f = open(user_db_path + userAccountNumber, 'r')

    except FileNotFoundError:
        print('User not found')
    except FileExistsError:
        print('User doesnt exist')
    except TypeError:
        print('Invalid number format')
    else:
        return f.readline()

    return False


def delete(userAccountNumber):
    isDeleteSuccessful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + '.txt'):

        try:
            os.remove(user_db_path + str(userAccountNumber) + '.txt')
            isDeleteSuccessful = True

        except FileNotFoundError:
            print('User not found')
        finally:
            return isDeleteSuccessful


def doesEmailExist(email):
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
        userList = str.split(read(user), ',')
        if email in userList:
            return True
    return False


def doesAccountNumberExist(accountNumber):
    allUsers = os.listdir(user_db_path)

    for user in allUsers:
        if user == str(accountNumber) + '.txt':
            return True
    return False


def authenticatedUser(accountNumber, password):
    if doesAccountNumberExist(accountNumber):
        user = str.split(read(accountNumber), ',')
        if password == user[3]:
            return user

    return False


# print(doesAccountNumberExist(9546415896))
# print(read({'One': 'Two'}))
