#foodlist is what our class objects can be
foodList = [('curry', 'spicy'), ('pavlova', 'sweet'), ('chips', 'salty')]
#creating a class to define our objects
class Food:
    def __init__(self, name, taste):
        #taking the arguements with self. to redefine them
        self.name = name
        self.taste = taste
def createFood(foodList):
    spicyfood = Food('curry', 'spicy')
    sweetfood = Food('pavlova', 'sweet')
    saltyfood = Food('chips', 'salty')
    return spicyfood,sweetfood,saltyfood
#using class Food will fill our arguments(name,taste)
#with what arguements we have put here


foodObjects = createFood(foodList)
##########################################
#foodlist is what our class objects can be
foodList = [('curry', 'spicy'), ('pavlova', 'sweet'), ('chips', 'salty')]
#creating a class to define our objects
class Food:
    
    def __init__(self, name, taste):
        #taking the arguements with self. to redefine them
        self.name = name
        self.taste = taste
        
    def __str__(self,str=' '):
        return (self.taste + str + self.name)
    
#passes foodlist so the list can be called.
def createFood(foodList):
    mylist = []
    for name,taste in foodList:
        mylist.append((taste,name))
    mylist = [str(x) + ' ' + str(y) for x, y in mylist]
    return mylist
        
        
foodObjects = createFood(foodList)
###################################
#foodlist is what our class objects can be
foodList = [('curry', 'spicy'), ('pavlova', 'sweet'), ('chips', 'salty')]
#creating a class to define our objects
class Food:
    
    def __init__(self, name, taste):
        #taking the arguements with self. to redefine them
        self.name = name
        self.taste = taste
        
    def __str__(self,str=' '):
        return (self.taste + str + self.name)

    def orderFood(self,i):
        print(i,"times", str(self))


#passes foodlist so the list can be called.
def createFood(foodList):
    mylist = []
    for name,taste in foodList:
        fooditem = Food(name,taste)
        mylist.append(fooditem)
    #mylist = [str(x) + ' ' + str(y) for x, y in mylist]
    return mylist
        
        
foodObjects = createFood(foodList)
##################################

#foodlist is what our class objects can be
foodList = [('curry', 'spicy'), ('pavlova', 'sweet'), ('chips', 'salty')]
#creating a class to define our objects
class Food:
    
    def __init__(self, name, taste):
        #taking the arguements with self. to redefine them
        self.name = name
        self.taste = taste
        
    def __str__(self,str=' '):
        return (self.taste + str + self.name)

    def orderFood(self,i):
        print(i,"times", str(self))
class NZFood(Food):
    origin = 'New Zealand'
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste
    def changeOrigin(self,origin):
        NZFood.origin = origin
        

#passes foodlist so the list can be called.
def createFood(foodList):
    mylist = []
    for name,taste in foodList:
        fooditem = Food(name,taste)
        mylist.append(fooditem)
    #mylist = [str(x) + ' ' + str(y) for x, y in mylist]
    return mylist
        
foodObjects = createFood(foodList)

f1 = NZFood('pavlova', 'sweet')
f2 = NZFood('chips', 'salty')
print(f1.origin)
print(f2.origin)
f1.changeOrigin('Aotearoa')
print(f1.origin)
print(f2.origin)

