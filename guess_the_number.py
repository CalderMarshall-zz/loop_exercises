import random
secret_number = random.randint(1,10)
print "I am thinking of a number between 1 and 10"
guess = int(raw_input ("What's the number?"))
play_again = raw_input("yes or no")
def number_game ():
while guess != secret_number:
    if guess > secret_number:
        print "Nope, try again"
        print "Too high"
    elif guess < secret_number:
        print "Nope, try again"
        print "Too low"
    guess = int(raw_input ("What's the number?"))
    if guess == secret_number:
        print "You Win!"
        play_again()
        break
play_again = raw_input("yes or no")
if play_again = "yes":
        number_game
elif play_again = "no":
    break
