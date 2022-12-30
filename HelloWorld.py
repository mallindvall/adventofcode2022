age1 = 12
age2 = 18
sent1 = "Today was a beautiful day"
firstName = "Malin"
lastName = "Lindvall"

## place holder
# %s for strings
# %d for integers
sent2 = "%s is 30 years old"
sent3 = "%s %s is cool"
sent4 = "%s is %d years old"
print(sent2%firstName)
print(sent3%("Malin", "Lindvall"))
print(sent4%("Malin", 30))