'''
Haruka Kido
haruka.kido@ndus.edu
CSCi 160 Spring 2020
Lab 2
'''

#Part 2. Convert from seconds
#one integer value: number of seconds
total = 20000

#calculate and display the number of equivalent hours, minutes, and seconds
hours = total // 3600 
total = total % 3600
minutes = (total-20) / 60
seconds = 20000 - ((hours*60*60) + (minutes*60))

#conversion of results into integers
hours = int(hours)
seconds = int(seconds)
minutes = int(minutes)

#print output statements
print('Seconds: 20000')
print('This is' , hours , 'hours,' , minutes , 'minutes' , 'and' , seconds , 'seconds.')




           
