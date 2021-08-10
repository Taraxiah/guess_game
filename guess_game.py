from random import randint

def check_input():
	max_val = 10
	while True:
		try:
			input_ = float(input("Please Enter An Integer between 1 and 10: "))
			input_ = int(input_)
		except ValueError:
			print("Invalid Input, Please Try Again...")
			continue
		else:
			if input_ < 1 or input_ > max_val:
				print("Please Provide A Number Between The Acceptable Range...")
				return check_input()
			else:
				return input_

def guess_game():
	random_value = randint(1, 10)
	attempts = 0

	while attempts < 3:
		input_ = check_input()
		if input_ > random_value:
			print("Your guess is higher than mine. Try Again")
			attempts = attempts+1
		elif input_ < random_value:
			print("Your guess is lower than mine. Try Again")
			attempts = attempts+1
		elif input_ == random_value:
			print("Congratulations! You guessed Correctly!")
			break

	if attempts == 3:
		print("Sorry, You Lost Because You Run Out Of Attempts")
		print("The Correct Number was: "+ str(random_value))


def main():
	continue_game = ["Yes", "yes", "Y", "y"]
	exit_game = ["No", "no", "N", "n"]
	
	guess_game()
	
	while True:
		play_again = input("Do You Wish To Play Again?")
		if play_again in continue_game:
			guess_game()
		elif play_again in exit_game:
			break
		else:
			print("I Do Not Understand")

if __name__ == "__main__" :
	main()
