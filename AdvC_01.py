""" Day 1 Advent of Code 2022 - Assignment 1"""

import requests

url = 'https://adventofcode.com/2022/day/1/input'

response = requests.get(url)
content = response.text

file_path = 'reindeer_calories.txt'

with open(file_path, 'w') as file:
    file.write(content)

print("Content saved to: ", file_path)