first_number = int(input("Enter first number:"))

second_number = int(input("Enter second number:"))

third_number = int(input("Enter third number:")) 
largest = first_number

if second_number > largest:
   largest = second_number 
   
  
if largest < third_number:
   largest = third_number
   print(largest)
else :
   print (largest)
 
