'''
docstring
comments about the file
Haruka Kido
haruka.kido@ndus.edu
Spring 2020. CSCi 160. In Class Lab 05. Th 7-9PM
'''

temp = int(input("What is the temperature in Celsius: "))

while temp != 999:
   if (temp < -25):#extremely cold
      print("The temperature entered is: Extremely cold")
      avg = 20

      far = abs(avg - temp) 
      print ("The temperature is" , far , "degrees away from the average temperature")

      F = temp * 1.8 + 32 
      print("The temperature" , temp , "Celsius is" , F , "in Fahrenheit")
      print()
   elif (temp > -24 and temp < 10): #cold
      print("The temperature entered is: Cold")
      avg = 20

      far = abs(avg - temp) 
      print ("The temperature is" , far , "degrees away from the average temperature")

      F = temp * 1.8 + 32
      print("The temperature" , temp , "Celsius is" , F , "in Fahrenheit")
      print()
   elif (temp > 11 and temp < 32): #warm
      print("The temperature entered is: Warm")
      avg = 20

      far = abs(avg - temp) 
      print ("The temperature is" , far , "degrees away from the average temperature")

      F = temp * 1.8 + 32
      print("The temperature" , temp , "Celsius is" , F , "in Fahrenheit")
      print ()
   elif (temp > 33): #extremely hot
      print("The temperature entered is: Extremely hot")
      avg = 20

      far = abs(avg - temp) 
      print ("The temperature is" , far , "degrees away from the average temperature")

      F = temp * 1.8 + 32
      print("The temperature" , temp , "Celsius is" , F , "in Fahrenheit")
      print()

   temp = int(input("What is the temperature in Celsius: "))
   if temp == 999:
      print ("<<program ends>>")
   



