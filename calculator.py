print("Welcome to Tommie calculator for basic math Operations.\n")

name = input("Can i know your name? ")
if name == 'no':
	print("\nLet's start calculating then, ") 
else:
	print(f"Enjoy your today's Calculations {name.title()}\n ")
	
	
def calculator(num1, num2, operation):
	"""Specifing the operations and their roles."""
	if operation == 'add':
		return num1 + num2
	elif operation == 'subtract':
		return num1 - num2
	elif operation == 'multiply':
		return num1 * num2
	elif operation == 'divide':
		# Making sure zero division error doesn't crash the program
		if num2 == 0:
			return "Error: Division by zero"
		else:
			return num1 / num2

#print(calculator(3, 5, 'add'))
#print(calculator(6, 0, 'divide'))

def get_input():
	"""Bringing in an input to allow users to continue with calculations."""
	while True:
		try:
			# User is prompt to enter two numbers and an operation.
			num1 = float(input("Enter your first number: "))
			num2 = float(input("Enter your second number: "))
			operation = input("Enter operation (add, subtract, multiply, divide ): ").lower()
			
			# To show the result as an output on the terminal.
			result = calculator(num1, num2, operation)
			print(f"Result: {result}")
			
			"""Asking the user whether they want to continue with
			calculations or stop and quit """
			continue_choice = input("Do you want to do another calculation? (yes/no): ").lower()
			if continue_choice != "yes":
				print("\nThanks for using my app.")
				print("Goodbye!")
				break
				
		# Making sure an Error doesn't stop the program.		
		except ValueError:
			print("Enter a valid number.")
		except Exception as e:
			Print(f"An error occurred: {e}")
			
get_input()
