# import the random package so that we can generate a random choice
from random import randint
from gamefunctions import winlose, gamelives

while gamelives.player is False:
	#set player to True
	print("______________________________________________________\n")
	print("Computer lives:", gamelives.computer_lives, "/", gamelives.total_lives, "\n")
	print("Player lives:", gamelives.player_lives, "/", gamelives.total_lives, "\n")
	print("Choose your weapon!\n") 
	print("______________________________________________________\n")
	
	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("\n"," the computer chose", gamelives.computer, "\n")
	print("player chose", player, "\n")
	
	if player.lower() == "quit":
		exit()
	elif gamelives.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if gamelives.computer == "paper":
			print("You lose!", gamelives.computer, "covers", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "smashes", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "paper":
		if gamelives.computer == "scissors":
			print("You lose!", gamelives.computer, "cuts", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "covers", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	elif player.lower() == "scissors":
		if gamelives.computer == "rock":
			print("You lose!", gamelives.computer, "smahses", player, "\n")
			gamelives.player_lives = gamelives.player_lives - 1
		else:
			print("You win!", player, "cuts", gamelives.computer, "\n")
			gamelives.computer_lives = gamelives.computer_lives - 1

	else:
		print("thats not a valid choice, try again")



	#handle all lives lost for player or AI
	if gamelives.player_lives is 0:
		winlose.winorlose("lost")
		# print("Out of lives! You suck at this game. Would you like to play again?")
		# choice = input("Y / N")
		# print (choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	#reset the game so we start over again
		# 	gamelives.player_lives = 5
		# 	gamelives.computer_lives = 5
		# 	player = False
		# 	gamelives.computer = choices[randint(0,2)]

	elif gamelives.computer_lives is 0:
		winlose.winorlose("won")
	# print("gamelives.Computer is out of lives! You rock at this game. Would you like to play again?")
	# choice = input("Y / N")
	# print (choice)

	# if (choice is "N") or (choice is "n"):
	# 	print("You chose to quit.")
	# 	exit()

	# elif (choice is "Y") or (choice is "y"):
	# 	#reset the game so we start over again
	# 	gamelives.player_lives = 5
	# 	gamelives.computer_lives = 5
	# 	player = False
	# 	gamelives.computer = choices[randint(0,2)]

	else:
		# need to check all of our conditions after checking for a tie

		gamelives.player = False
		gamelives.computer = gamelives.choices[randint(0, 2)]
