# Python Program to find the factors of a number

# define a function
import math
num = int(raw_input("Find factors of what number?"))

   # This function takes a number and prints the factors


for i in range(1, int(math.sqrt(num))):
    if x % i == 0:
        print(i)

# change this value for a different result.

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))
