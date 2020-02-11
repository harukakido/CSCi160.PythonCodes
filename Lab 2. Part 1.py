'''
Haruka Kido
haruka.kido@ndus.edu
CSCi 160 Spring 2020
Lab 2
'''

#Part 1. Convert to seconds
#prompt user to enter three integers for hours, minutes and seconds
hours = int(input("Please enter an integer for hours: "))
minutes = int(input("Please enter an integer for minutes: "))
seconds = int(input("Please enter an integer for seconds: "))

#calculate and display the number of equivalent seconds
total_seconds = 60*60*(hours) + 60*(minutes) + (seconds)

#print integer variables as output statements
print('Hours:' , hours)
print('Minutes:' , minutes)
print('Seconds:' , seconds)

#print total seconds as output statement
print(total_seconds, 'seconds')

