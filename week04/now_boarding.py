passengers = [ "Frodo", "Sam", "Gandalf", "Smeagol" ]

airplane_has_rows = 2
each_row_has_seats = 2
first_col_label = 65 # ASCII 'A'


"""
Frodo    1A
Sam      1B
Gandalf  2A
Smeagol  2B
"""

for i in range(len(passengers)):
    row = (i//each_row_has_seats)+1
    col = chr(first_col_label + i%each_row_has_seats)
    print(f"{passengers[i]:<10} {row}{col}")
