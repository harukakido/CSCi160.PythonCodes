'''
Haruka Kido
haruka.kido@ndus.edu
CSCi 160 Spring 2020
Lab 2
'''

#Part 2. Convert from seconds
#prompt user to enter one integer value: total number of seconds
total_1 = int(input("Please enter an integer for total number of seconds: "))

#calculate and display the number of equivalent hours, minutes, and seconds
hours = total_1 // 3600 
total = total_1 % 3600 
minutes = total // 60
seconds = total_1 - ((hours*60*60) + (minutes*60))

#conversion of results into integers
hours = int(hours)
seconds = int(seconds)
minutes = int(minutes)

#print output statements
print('Seconds:' , total_1)
print('This is' , hours , 'hours,' , minutes , 'minutes' , 'and' , seconds , 'seconds.')




           
