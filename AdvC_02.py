"""Day 2 Advent of Code 2022 - Assignment 1"""

list_of_games = []
opponent_score = 0
my_score = 0

game_card = open('input_day2.txt').read().split('\n')

for game in game_card:
    list_of_games.append(game.split())


for game in list_of_games:
    opponent_sign, my_sign = game
    if opponent_sign == 'A' and my_sign == 'Z':
        opponent_score += 1 + 6
        my_score += 3
    elif opponent_sign == 'A' and my_sign == 'Y':
        opponent_score += 1
        my_score += 2 + 6
    elif opponent_sign == 'A' and my_sign == 'X':
        opponent_score += 1 + 3
        my_score += 1 + 3
    elif opponent_sign == 'B' and my_sign == 'X':
        opponent_score += 2 + 6
        my_score += 1
    elif opponent_sign == 'B' and my_sign == 'Y':
        opponent_score += 2 + 3
        my_score  += 2 + 3 
    elif opponent_sign == 'B' and my_sign == 'Z':
        opponent_score += 2
        my_score += 3 + 6
    elif opponent_sign == 'C' and my_sign == 'X':
        opponent_score += 3
        my_score += 1 + 6
    elif opponent_sign == 'C' and my_sign == 'Y':
        opponent_score += 3 + 6
        my_score += 2
    elif opponent_sign == 'C' and my_sign == 'Z':
        opponent_score += 3 + 3
        my_score += 3 + 3                 
    else:
        print("no mapped score")

print(f' My score was {my_score}, my opponents score was: {opponent_score}')

