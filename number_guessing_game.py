import random

name = input("What is your name? ")
print(f"Welcome to number guessing {name.title()}\n")



def number_guessing_game():
	"""Initializing the number guessing game."""
	number_to_guess = random.randint(1, 100) # setting the range of numbers to guess
	# indicating starting point of attempts to guess
	attempts = 0
	
	while True: # creating a loop to keep prompting the user again & again.
		try: 
			# prompting the user for a number to guess
			guess = int(input("Enter a number: "))
			""" 
			   Adding the total number of attempts every time the user
			   tries to guess a number.
			"""			
			attempts += 1
			
			# Using a conditional statement to determine the number to guess.
			if guess > number_to_guess:
				print("Too High! try again.")
			elif guess < number_to_guess:
				print("Too Low! try again.")
			else:
				# Print this statement if guess is right.
				print(f"Congratulations! {name.title()}, you guessed it right in {attempts} attempts.")
				# when the number guess is correct stop the loop.
				break
		except ValueError:
			""" 
				making sure the program continues running though a letter is entered
				instead of a number.
			"""
			print("Invalid value! please enter a valid number.")
# This line calls the function			
number_guessing_game()
