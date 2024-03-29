"""Day 3 Advent of Code 2022 - Assignment 1"""

import string

my_score = 0

character_value_dict = dict(zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53)))

list_from_rugsack = open('input_day3.txt').read().splitlines()

for line in list_from_rugsack:
    first_half, second_half = line[:int(len(line)/2)], line[int(len(line)/2):]
    common_words = ''.join(set(first_half).intersection(second_half))
    my_score += character_value_dict[common_words]

print(f'My first score: {my_score}')


"""Day 3 Advent of Code 2022 - Assignment 2"""
my_second_score = 0

    
for item in range(0,len(list_from_rugsack)-2, 3):
    set1 = set(list_from_rugsack[item])
    set2 = set(list_from_rugsack[item + 1])
    set3 = set(list_from_rugsack[item + 2])
    common_char = ', '.join(list(map(str, set1.intersection(set2, set3))))
    my_second_score += character_value_dict[common_char]

print(f'My second score: {my_second_score}')

