"""

control statement:-

if
if_else
if_else  nested


---loops

for 
while




*** empty values behave like False ( i.g: '', {}, [], 0), rest behave like True

"""


print("----------if")

"""
    if(boolean) =>

    eg:
        if( 2 < 3)

        if( fileName ==="bah.sh" )
"""

fileName = "errorlogs.json"  # info.txt

if fileName == "errorlogs.txt":
    print("error logs exists")

print("--------------eg-1")
num = 2
if num > 3:
    print(" num is less than 3")


print("----------if else")

if fileName == "errorlogs.txt":
    print("error logs exists")
else:
    print("no error logs")


print("eg 2=================")

salary = 1000

if salary < 100000:
    print("salary is less than 1lac")

else:
    print(" salary is not less than one lakh")


print("-------------------nested ----------")

print("==========================GST===================================")

"""
GST slabs

< 5 lacs - no tax
< 7.5 lacs - 5% tax
< 10 lacs - 10% tax
< 15 lacs - 15% tax
> 20 lacs - 30% tax

"""

salary = 22000002

if salary < 500000:
    print(" no tax ")
elif salary <= 750000:
    print(" 5 % tax")
elif salary <= 1000000:
    print(" 10% tax")
elif salary <= 1500000:
    print(" 15% tax")
else:
    print(" 30% tax")

print("==========================GST===================================")

"""
Cred coins -> game

"""
print()
print("==========================Cred coins===================================")

paidAmount = 11000

if paidAmount > 10000:
    print(" you are elgible for cred play cash back")
    spinNumber = 777
    if spinNumber == 777:
        print(" you won the Apple moile")
    else:
        print(" normal cash back")
else:
    print(" not eligible for cashback")


print("-------------------------------------------------------")
name = ""
if name:
    print(" name exists")
else:
    print(" name not exists")


name = "Rama"
if name:
    print(" name exists")
else:
    print(" name not exists")
