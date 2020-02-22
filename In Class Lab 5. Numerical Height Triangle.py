'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. In Class Lab 05B. Th 7-9PM
'''

height = int(input("Enter height: "))
for row in range(height, 0, -1):
    for column in range(row+1):
        print (column, end=' ')
    print( )
