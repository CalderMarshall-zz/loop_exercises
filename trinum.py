# funciton showing triangle numbers
#xn = n(n+1)/2
#desired triangle sequence marker number will be n
import math
n = int(raw_input("Find amount of dots for which sequence marker?"))
def total_dots(n):
    print n*(n+1)/2
total_dots(n)
