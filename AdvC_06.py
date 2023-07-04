

with open('input_06.txt', 'r') as file:
    input_file = file.read()


# ==== PART 1 ====

for input in range(4, len(input_file)): #move from the 5th character to the end of the input
    block = set(input_file[(input -4): input]) #take the charachters before the 5th character upuntil the 5th character. Set cannot contain duplicates. Will only displat unique characters.
    if len(block) == 4:
        print(f'Answer for part 1 is: {input}')
        break

# ==== PART 2 ====    

for input in range(14, len(input_file)): 
    block = set(input_file[(input -14): input])
    if len(block) == 14:
        print(f'Answer for part 2 is: {input}')
        break