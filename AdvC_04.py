"""Day 4 Advent of Code 2022 - Assignment 1"""

input_file = open('input_04.txt', 'r').readlines()
count_contains_subset = 0

for item in input_file:
    first_part, second_part = item.split(',')
    start_value_first_part, stop_value_first_part = first_part.split('-')
    start_value_second_part, stop_value_second_part = second_part.split('-')
    range_values_first_part = set(range(int(start_value_first_part), int(stop_value_first_part) +1))
    range_values_second_part = set([value for value in range(int(start_value_second_part), int(stop_value_second_part)+1)])
    

    if (range_values_first_part.issubset(range_values_second_part) or range_values_second_part.issubset(range_values_first_part))  :
        count_contains_subset += 1


print(count_contains_subset)

"""Day 4 Advent of Code 2022 - Assignment 2"""

count_contains_same_value = 0

for item in input_file:
    first_part, second_part = item.split(',')
    start_value_first_part, stop_value_first_part = first_part.split('-')
    start_value_second_part, stop_value_second_part = second_part.split('-')
    range_values_first_part = set(range(int(start_value_first_part), int(stop_value_first_part) +1))
    range_values_second_part = set([value for value in range(int(start_value_second_part), int(stop_value_second_part)+1)])

    if range_values_first_part.intersection(range_values_second_part):
        count_contains_same_value += 1
    

print(count_contains_same_value)

