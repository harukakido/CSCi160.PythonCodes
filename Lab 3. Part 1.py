'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 02. Th 7-9PM
'''

#Part 1
#have the user enter a numeric value
n = float(input("Please enter a numeric value: "))

#for the entered number, tell if:
#a)the value is a whole number
if n - int(n) != 0:
   print (n, "is not a whole number")
elif int(n) - int(n) == 0:
   print (int(n), "is a whole number")   
   
#b)the value is, or is not, a multiple of 5
if n % 5 != 0:
   print (n, "is not a multiple of 5")
elif n % 5 == 0:
   print (n, "is a multiple of 5")
   
#c)the value is even or odd
if int(n) % 2 == 0:
   print (n, "is even")
elif int(n) % 2 != 0:
   print (n, "is odd")
   
#d)the value is positive, negative, or zero
if n>0:
   print (n, "is positive")
if n<0:
   print (n, "is negative")
elif n == 0:
   print (n, "is zero")
   
#e)the value is, or is not, within the range of 2010 to 2019 inclusive
if n >= 2010 and n <= 2019:
   print (n, "is within the range of 2010 to 2019 inclusive")
else:
   print (n, "is not within the range of 2010 to 2019 inclusive")
   
#f)the value is, or is not, within the 100's, meaning is it a three-digit number which starts with 1
#considering digits as all values starting from left of the decimal point if decimal point present
#digits include 0
if n >= 100 and n < 200:
   print (n, "is within the 100's")
else:
   print (n, "is not within the 100's")

   print()

#then have the user enter a text value
str = str(input("Please enter a text value: "))

#for the entered text, tell: 
#g)how many characters are in the string
character_count = len(str)
print (str, "has" , character_count , "characters")

#h)if the string entered is "yes", "no", or neither of those words (case-specific)
if str == 'yes':
   print (str, 'is "yes"')
   
if str == 'no':
   print (str, 'is "no"')
   
elif str != 'yes' and str != 'no':
   print (str, "is neither yes or no")
   
#i)if the string entered is 'yes', either upper- or lower-case
if str == 'yes':
   print (str, "is yes, all lower-case")
   
if str == 'YES':
   print (str, "is YES, all upper-case")
   
elif str != 'yes' and str!= 'YES':
   print (str, "is not yes or YES")
   
#j)if the string starts with a lower case 'a'
#alpha2num
if str.startswith(('a')):
   print (str, "does start with an 'a'")

if str.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P,', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
   print (str, "does not start with an 'a'")
   


   