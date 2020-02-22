for student in range(1,4):
   name = input("Enter Student Name " + str(student)+ ": ")
   total = 0
   for val in range(1,4):
      score = int(input("Enter score " + str(val) + ": "))
      total += score
   average = total/3
   print ("Name: " , name)
   print("Average: " , average)
   print()
