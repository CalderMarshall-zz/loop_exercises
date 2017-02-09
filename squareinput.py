width = int(raw_input("Enter width"))
height = int(raw_input("Enter height"))

for i in range (height):
    if i:
        print("*"*(width))
    else:
     print ((width) * "*")
