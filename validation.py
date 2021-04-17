def accountNumberValidation(accountNumber):
    if accountNumber:

        try:
            int(str(accountNumber))
            if len(str(accountNumber)) == 10:
                return True

        except ValueError:
            # print('Invalid Account Number')
            return False
        except NameError:
            # print('Invalid')
            return False

    return False
