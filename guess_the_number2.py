secret_number = 5
print "I am thinking of a number between 1 and 10"
while True:
    guess = int(raw_input("What's the number?"))
    if guess == secret_number:
        print "You Win!"
        break
    else:
        print "Nope, try again"
