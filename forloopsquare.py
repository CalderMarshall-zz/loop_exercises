
N = int(raw_input("How big is the square?"))
this_width = int(raw_input("Width?"))
this_height = int(raw_input("Height?"))
print "*" * this_width
for i in range(this_height - 2):
    print "*" * (this_width - 2) "*" * (this_height - 2)
print "*" * this_width
#for char in range(N):
    #print "*" * N

# this_string = "*****"
# for char in this_string:
#     print char * N
