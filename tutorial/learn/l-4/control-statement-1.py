"""

control statement:-

if
if_else
if_else  nested


---loops

for 
while

"""


print("----------if")

"""
    if(boolean) =>

    eg:
        if( 2 < 3)

        if( fileName ==="bah.sh" )
"""

fileName = "errorlogs.txt" # info.txt

if(fileName == 'errorlogs.txt'):
  print('error logs exists')


print('----------if else')

if(fileName == 'errorlogs.txt'):
  print('error logs exists')
else:
     print("no error logs")  


print("eg 2=================")

salary = 10000

if(salary < 100000):
   print("salary is less than 1lac")

else:
   print(" salary is not less than one lakh")
   

print("-------------------nested ----------")


       
"""
GST slabs

< 5 lacs - no tax
< 7.5 lacs - 5% tax
< 10 lacs - 10% tax
< 15 lacs - 15% tax
> 20 lacs - 30% tax

"""

salary = 100000

if(salary < 500000):
  print( " no tax ")
elif(salary < 750000):
  print(" 5 % tax")
elif(salary < 1000000):
  print(" 10% tax")   
elif(salary < 1500000):
  print(" 15% tax")
else:
  print(" 30% tax")     



"""
Cred coins -> game

"""

paidAmount = 11000

if(paidAmount > 10000):
  print(" you are elgible for cred play cash back")
  spinNumber = 123
  if(spinNumber == 777):
    print(" you won the Apple moile")
  else:
    print(" normal cash back")  
else:
  print(" not eligible for cashback")
