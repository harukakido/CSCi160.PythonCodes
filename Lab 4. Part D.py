'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 04. Th 7-9PM
'''

#Part D
#small, single value multiplication table using a for loop
#ask for a value between 1 and 10
value = int(input("Enter a number between 1 and 10: "))
print ()

#if input value is less than 1 or greater than 10
#display error message stating input is invalid 
#terminate program
import sys
if value < 1:
   sys.exit("Error: Input is invalid")

if value > 10:
   sys.exit("Error: Input is invalid")

#if input value is valid
#display table showing result of multiplying the input value times the numbers 1-10

#label top of table with "Multiplication table for input value" 
print ("Multiplication table for", value)
print ()

#initialize multiplier with input into equations
#right justify all columns of numbers
#right justified by width 3 to include proper right justification if input value is 10
multipliers = {
   ' 1': str(value) + " = " + str(value).rjust(3),
   ' 2': str(value) + " = " + str(2*value).rjust(3),
   ' 3': str(value) + " = " + str(3*value).rjust(3),
   ' 4': str(value) + " = " + str(4*value).rjust(3),
   ' 5': str(value) + " = " + str(5*value).rjust(3),
   ' 6': str(value) + " = " + str(6*value).rjust(3),
   ' 7': str(value) + " = " + str(7*value).rjust(3),
   ' 8': str(value) + " = " + str(8*value).rjust(3),
   ' 9': str(value) + " = " + str(9*value).rjust(3),
   '10': str(value) + " = " + str(10*value).rjust(3),
}

for v in multipliers:
   print ("{} * {}".format(v, multipliers[v]))