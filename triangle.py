num_rows = int(raw_input("How tall?"))
def pyramid(rows=num_rows):
    for i in range(rows):
        print ' '*(rows-i-1) + '*'*(2*i+1)
pyramid(num_rows)
