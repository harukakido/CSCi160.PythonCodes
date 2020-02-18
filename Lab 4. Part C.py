'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. Lab 04. Th 7-9PM
'''

#Part C
#program asks for integer values until the user enters 0
value = int(input("Enter a Value: "))
positive_sum = 0 #positive numbers sum
negative_sum = 0 #negative numbers sum
positive_count = 0 #positive numbers count
negative_count = 0 #negative numbers count

while(value != 0): #establishes all numbers except 0 as loop condition
   if(value > 0): #positive
      positive_count = positive_count + 1
      positive_sum = positive_sum + value
   else: #negative
      negative_count = negative_count + 1
      negative_sum = negative_sum + value
   value = int(input("Enter a Value: ")) #continues loop with valid input conditions
      
#display average of entered positive values
#output average with 2 places after decimal point
if(positive_count > 0):
   average_pos = format(positive_sum/positive_count,"5.2f")
   print("Average of positive values: ", str(average_pos).rjust(8))
else:
   print("Average of positive values: No positive values entered")

#display average of entered negative values
#output average with 2 places after decimal point
if(negative_count > 0):
   average_neg = format(negative_sum/negative_count,"5.2f")                   
   print("Average of negative values: ", str(average_neg).rjust(8))
else:
   print("Average of negative values: No negative values entered")
