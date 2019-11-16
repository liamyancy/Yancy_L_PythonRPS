from random import randint
from gamefunctions import gamelives
def winorlose(status):
	# status will be either won or lost
	print("called win or lose")
	print("______________________________________________________")

	print("You", status, "! Would you like to play again?")

	gamelives.choice = input("Y / N ")
	print (choice)

	if (choice is "N") or (choice is "n"):
		print("You chose to quit.")
		exit()

	elif (choice is "Y") or (choice is "y"):
		#reset the game so we start over again

		gamelives.player_lives = 5
		gamelives.computer_lives =5
		gamelives.total_lives = 5
		gamelives.player = False
		gamelives.computer = gamelives.choices[randint(0,2)]

	else:
		print("make a valid choice, Y or N")
		# use recursion to call winorlose again
		winorlose(status)