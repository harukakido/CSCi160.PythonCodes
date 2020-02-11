'''
Haruka Kido
haruka.kido@ndus.edu
CSCi 160 Spring 2020
Lab 2
'''

#Part 3. Convert to dollars
#prompt user to enter four integers: quarters, dimes, nickels, and pennies
quarters = int(input("Please enter an integer for the amount of quarters: "))
dimes = int(input("Please enter an integer the amount of dimes: "))
nickels = int(input("Please enter an integer for the amount of nickels: "))
pennies = int(input("Please enter an integer for the amount of pennies: "))

#calculation of total number of cents
total_number_of_cents = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)) - ((quarters*25) + ((dimes*10) - 10))

#conversion from cents to dollars by dividing by 100.0
cents_to_dollars = total_number_of_cents / 100.0

#equivalence in dollars and cents
equivalence_in_dollars_and_cents = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)) / (100.0)

#print output statements
print('Quarters:' , quarters)
print('Dimes:' , dimes)
print('Nickels:' , nickels)
print('Pennies:' , pennies)
print('This is equal to $', equivalence_in_dollars_and_cents)

