age1 = 12
age2 = 18
sent1 = "Today was a beautiful day"
firstName = "Malin"
lastName = "Lindvall"

###### place holders

# %s for strings
# %d for integers
sent2 = "%s is 30 years old"
sent3 = "%s %s is cool"
sent4 = "%s is %d years old"
#print(sent2%firstName)
#print(sent3%("Malin", "Lindvall"))
#print(sent4%("Malin", 30))

###### Lists/Arrays

shopList = ["Apples", "Oranges", "Bananas", "Cheese"]
# print(shopList[2]) print object in list
shopList.append("Blueberries") #add more to list - append
shopList[0] = "Cherries" # changes value in list - apples to cherries
del shopList[1] # delete object in array - oranges

###### Dictionaries

### key value pairs - each key should be unique
students = {"Bob":12, "Rachel": 13, "Emily": 15}
#print(students["Rachel"])
students["Rachel"] = 15 # changing value of rachel
#print(students["Rachel"])

###### Tuples
### list that are immutable (cannot be changed). 2 tuples can be added together
tup = ("Oranges", "Apples", "Bananas")

###### Conditional Statements

if (age1 < 3) :
    print("Hello")
elif(age1 > 3):
    print("Stay!")
else:
    print("Bye Bye")

###### For Loops

list1 = ["Apples", "Bananas", "Cherries"]
tup1 = (13,12,15)

for item in list1: 
    print(item)

for item in tup1:
    print(item)

## range function
for i in range(0,10):
    print(i)

## range function
for i in range(0,11,2): #skipping every second number, increments by 2
    print(i)