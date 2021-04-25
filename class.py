class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You successfully deposited {} in {} category".format(amount, self.category)

    def budgetBalance(self):
        return 'This is the current balance: {}'.format(self.amount)

    def checkBalance(self):
        #return a boolean, check if amount is less or greater than self.amount
        if self.budgetBalance < self.amount:
            return 'You are below your budget with balance of {}'.format(self.amount)
        else: #self.budgetBalance >= self.amount:
            return 'You are within balance'
    

    def withdrawal(self, amount):
        #reverse of deposit
        self.amount -= amount
        return 'You successfully withdrew {} in {} category'.format(amount, self.category)
        

    def transfer(self, amount, category):
        #transfer between instantiated categories
        return self.withdrawal(amount) + ',' + category.deposit(amount)


foodCategory = Category ('Food', 1000)
clothingCategory = Category ('Clothing', 300)
rentCategory = Category ('Rent', 800)
entertainmentCategory = Category('Entertainment', 500)

#print(foodCategory.withdrawal(250))
#print(foodCategory.budgetBalance())
#print(rentCategory.deposit(500))
#print(rentCategory.budgetBalance())
#print(foodCategory.transfer(100, rentCategory))
#print(foodCategory.budgetBalance())
print(clothingCategory.withdrawal(500))
print(clothingCategory.checkBalance())