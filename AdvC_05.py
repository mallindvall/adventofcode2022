#input_file = open('input_day5.txt', 'r').readlines()

#slice - visar värden i input_file från element 0 - 8. input_file.index(osv.) för in 9 som slice siffra, \n är på index 9. 
# vill ej ha med den raden, därav -1. "Står input_file[0:8]"
#crate_lines = input_file[:input_file.index('\n')-1] 

#slice - ta ut att det är 9 kolumner. 
#[:input_file.index('\n')] tar ut alla värden i kolumn sektionen. Utifrån det urvalet [-1] för att ta ut sista raden (visar 1-9) [-3] för att ta ut 9an som
#som är 3dje sista värdet
#number_of_crates = input_file[:input_file.index('\n')][-1][-3] 

#moving_lines = input_file[input_file.index('\n')+1:]

#for line in moving_lines:
#    amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]

####### FROM YOUTUBE SOLUTION #####################
# === source: https://www.youtube.com/watch?v=LvH2DU1bARk ====

with open('input_day5.txt') as input_file:
     stack_strings, instructions = (i.splitlines() for i in input_file.read().strip('\n').split('\n\n'))


stacks = {int(digit):[] for digit in stack_strings[-1].replace(' ', '')} #creates a dicitionary, which contains a list per stack value (1-9)
indexes = [index for index, values in enumerate(stack_strings[-1])if values != ' ']


def displayStacks():
    for stack in stacks:
        print(stack, stacks[stack])

def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != ' ':
                stacks[stack_num].insert(0,string[index])
            stack_num += 1

def getStackEnds():
    final_string = ''
    for stack in stacks:
        final_string += stacks[stack][-1]
    print(final_string)


def emptyStack():
    for value in stacks:
        stacks[value] = []
  


# ==== PART 1 ====
loadStacks()

for instruction in instructions:
    moves, source, target = [int(entry) for entry in instruction.strip().split(' ') if entry.isdigit()]

    for move in range(moves):
        crate_removed = stacks[source].pop()
        stacks[target].append(crate_removed)


#displayStacks()
getStackEnds() 

 # ===== PART 2 =====

emptyStack()
loadStacks()

for instruction in instructions:
    moves, source, target = [int(entry) for entry in instruction.strip().split(' ') if entry.isdigit()]

    crates_to_remove = stacks[source][-moves:] # finding out which crates to move
    stacks[source] = stacks[source][:-moves] # removing crates

    for crate in crates_to_remove:
        stacks[target].append(crate) # adding crates to different stack

displayStacks()
getStackEnds() 


