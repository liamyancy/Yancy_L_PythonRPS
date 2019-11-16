from random import randint

player_lives = 5
computer_lives = 5
total_lives = 5

# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based -> first entry is 0, 2nd is `, 3rd is 2 etc
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of these choices
computer = choices[randint(0, 2)]

# set up the game loop so that we don't have to restart all the time
player = False