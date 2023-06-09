""" Day 1 Advent of Code 2022 - Assignment 1"""
"""Find the elf carrying the most calories - how many calories is that one carrying?"""

total_calories_per_elf = []

elves = open('elves_calories.txt').read().split('\n\n') #splits file on double new lines, it contains one list where each elf is separated by ', '

for elf in elves:
    total_calories_per_elf.append(sum(map(int, elf.split()))) #default split() splits on ' ' which is the element beween elfs. map converts the text elements in the list to int. 

print(f'Number of calories top elf is carrying: {max(total_calories_per_elf)}') # answer part 1


"""Day 1 Advent of Code 2022 - Assignment 2"""
"""Find the top 3 elves carrying the most calories how much is that in total?"""

total_calories_per_elf_sorted = sorted(total_calories_per_elf, reverse = True)

print(f'Number of calories top 3 elves are carrying: {sum(total_calories_per_elf_sorted[:3])}') # answer part 2