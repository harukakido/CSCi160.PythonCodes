'''
Haruka Kido
haruka.kido@ndus.edu
CSCi 160 Spring 2020
Lab 2
'''

#Part 3. Convert to dollars
#four integers: quarters, dimes, nickels, and pennies
quarters = 6
dimes = 6 
nickels = 6 
pennies = 6

#calculation of total number of cents
total_number_of_cents = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)) - ((quarters*25) + ((dimes*10) - 10))

#conversion from cents to dollars by dividing by 100.0
cents_to_dollars = total_number_of_cents / 100.0

#equivalence in dollars and cents
equivalence_in_dollars_and_cents = ((quarters*25) + (dimes*10) + (nickels*5) + (pennies*1)) / (100.0)

#print output statements
print('Quarters: 6')
print('Dimes: 6')
print('Nickels: 6')
print('Pennies: 6')
print('This is equal to $', equivalence_in_dollars_and_cents)

