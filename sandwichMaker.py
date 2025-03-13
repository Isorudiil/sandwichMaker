import pyinputplus as pyip


def cheeseAndCondiments(dict):
    cheeses = {
    'american': 50,
    'cheddar': 100,
    'swiss': 125,
    'provolone': 150
}
    condiments = 100
    match dict:
        case {'cheeses': 'yes', 'condiments': 'yes'}:
            return cheeses[dict['type']] + condiments
        case {'cheeses': 'no', 'condiments': 'yes'}:
            return condiments
        case {'cheeses': 'no', 'condiments': 'no'}:
            return 0


breads = {
    'white': 100,
    'wheat': 150,
    'sourdough': 200,
    'rye': 50
}
proteins = {
    'chicken': 300,
    'beef': 250,
    'ham': 200
}

# empty dict to hold cheese and condiments information to pass to cheeseAndCondiments()
chsAcond = {}

# create inputMenu() for bread types
breadType = pyip.inputMenu(['white', 'wheat', 'sourdough', 'rye'])
print('\n')

# create inputMenu() for protein types
proteinType = pyip.inputMenu(['chicken', 'beef', 'ham'])
print('\n')

# create inputYesNo() for cheese
cheese = pyip.inputYesNo('Would you like cheese?\n')
print('\n')

# create inputMenu() for cheese types if inputYesNo() is 'Y'
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['american', 'cheddar', 'swiss', 'provolone'])
    print('\n')
    chsAcond.update({'cheeses': 'yes', 'type': cheeseType})
else:
    cheeseType = 'no'
    chsAcond.update({'cheeses': 'no'})

# create inputMenu() for condiment types
condiments = pyip.inputYesNo('Would you like mayo, mustard, lettuce, or tomato?\n')
print('\n')

if condiments == 'yes':
    chsAcond.update({'condiments': 'yes'})
else:
    chsAcond.update({'condiments': 'no'})

# create inputInt() for quantity of sandwiches
quantity = pyip.inputInt('How many sandwiches would you like?\n')

# TODO: create prices for all options and calculate total (be sure to include multiple sammies)
total = (breads[breadType] + proteins[proteinType] + cheeseAndCondiments(chsAcond)) * quantity

print(f'Your total is ${total / 100:.2f}')


# print('''
# Bread: %s
# Protein: %s
# Cheese: %s
# Condiments: %s
# Quantity: %s''' % (breadType, proteinType, cheeseType, condiments, quantity))