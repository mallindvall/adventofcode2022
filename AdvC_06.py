
#example input:  qwerrttjfkfld
#take first 4 characters in string > see if they are unique
# if yes take the index at the last character in the string (+1)
# if not move one character ahead in the string and make the same comparison

input_file = open('input_06.txt', 'r').readlines()

counter = 0
run = True
run_2 = True
stop_index = []
stop_index_2 = []

def has_multipte_characters(input_to_compare):
    characters_count = {}
    for char in input_to_compare:
        if char in characters_count:
            return True
        characters_count[char] = 1
    return False


# ==== PART 1 ====


for input in input_file:   
    for element in input:
        while run == True:
            input_to_compare = input[counter:counter + 4]
            counter += 1
            if has_multipte_characters(input_to_compare) == False: 
                run = False
            stop_index.append(element)
            

print(len(stop_index)+3)

     
# ==== PART 2 ====
        
for input in input_file:   
    for element in input:
        while run_2 == True:
            input_to_compare_message = input[counter:counter + 14]
            counter += 1
            if has_multipte_characters(input_to_compare_message) == False: 
                run_2 = False
            stop_index_2.append(element)
            
print(len(stop_index_2)+ 13)       
        
        
        
        
        
        
        
        
        
'''
if input_to_compare.count(element) > 1:
    print('yes', input_to_compare, element) 
else: print('no', input_to_compare, element)
counter += 1
 '''
        