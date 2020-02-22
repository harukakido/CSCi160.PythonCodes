'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. In Class Lab 05. Th 7-9PM
'''

num1 = int(input("What is row number: "))
num2 = int(input("What is column number: "))
num_rows=7
num_cols=5
for row in range(1, num1):
    for col in range(num2):
        print ("*",end= " ")
    print()
