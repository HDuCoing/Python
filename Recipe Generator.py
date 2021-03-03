import random

main_ingredient = ['chocolate', 'banana', 'salted caramel', 'carrot', 'bran']
baking = ['cake', 'brownie', 'cupcake', 'muffin']
measure = ['tbsp', 'tsp', 'cup', 'mls']
ingredient = ['flour', 'baking powder', 'butter', 'milk', 'eggs', 'vanilla', 'sugar']
quantity = random.randint(1,3)
temp = random.randint(170,220)
time = random.randint(10,60)

def main():
    mingred = random.choice(main_ingredient)
    bak = random.choice(baking)
    quantity = random.randint(1,3)
    meas = random.choice(measure)
    print('***', mingred, bak, 'Recipe', '***')
    print("Ingredients:")
    print(quantity, meas, mingred)

def recipe():
    meas = random.choice(measure)
    ingredi = random.choice(ingredient)
    quantity = random.randint(1,3)
    print(quantity, meas, ingredi)
def method():
    a, b, c, d, e = [random.choice(ingredient), random.choice(ingredient), random.choice(ingredient), random.choice(ingredient), random.choice(ingredient)]
    mingred = random.choice(main_ingredient)
    bak = random.choice(baking)
    temp = random.randint(170,220)
    time = random.randint(10,60)
    print('Method:')
    print('Mix the', a, b, c, d, 'and', e, 'together.')
    print('Gently fold in the', mingred,'.') 
    print('Place mixture in', bak, 'tin and bake at', temp,'degrees Celsius for', time,'minutes.')

main()
for x in range(5):
    recipe()
method()
