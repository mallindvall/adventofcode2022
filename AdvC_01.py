""" Day 1 Advent of Code 2022 - Assignment 1"""

total = []

elves = open('elves_calories.txt').read().split('\n\n') #splits file on double new lines, it contains one list where each elf is separated by ', '

for elf in elves:
    total.append(sum(map(int, elf.split()))) #default split() splits on ' ' which is the element beween elfs. map converts the text elements in the list to int. 

print(max(total))
