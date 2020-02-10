'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 02. Th 7-9PM
'''

#Part 2
#convert number input to english text output
#number dictionary
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero'}

#asks user to input a number between 20 and 99
n = int(input("Please enter an integer value between 20 and 99: "))

if n >= 21 and n <= 29:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 31 and n <= 39:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 41 and n <= 49:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 51 and n <= 59:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 61 and n <= 69:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 71 and n <= 79:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 81 and n <= 89:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")

if n >= 91 and n <= 99:
      print ("The number is" , num2words[n-n%10] + " " + num2words[n%10].lower() + ".")
      
if n == 20:
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 30:
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 40: 
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 50:
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 60: 
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 70:
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 80:
      print ("The number is" , num2words[n-n%10] + ".")
      
if n == 90:
      print ("The number is" , num2words[n-n%10] + ".")

elif n < 20:
      print ("The number is not within a valid range.")
      
elif n > 99:
      print ("The number is not within a valid range.")