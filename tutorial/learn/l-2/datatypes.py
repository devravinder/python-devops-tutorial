
"""
Multi line comment

ref: https://www.w3schools.com/python/python_datatypes.asp

---
Text,
Number,
Boolean


----
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


----- Imp
int, float
list
dist
bool


"""

name = "ravinder" # string
age = 26
exp = 4.2


print(name, age, exp)


print('+++++++++++++++++++++++++++++++++++++++++++++++++')

print("name:", name, "age:", age, "exp:", exp)

print("type of name", type(name))


print("-----------------")
isHeWorking = True  

"""

isHeWorking -> camel case
is_he_working -> snake case

"""

isHeManager = False

print(isHeWorking, isHeManager)

print()

firstJob, secondJob, thirdJob = "uttara",'Durvah', "BUHL" # declaring multiple variables ( not imp )

print("firstJob ", firstJob, ",secondJob ", secondJob, ",thirdJob", thirdJob)

print()

print("============= list ============")
# -------------------------

fruits = ["apple", "banana", "cherry", "cherry"] # list
  # index:   0      ,   1,     2,          3

#display x:
print(fruits)

#display the data type of x:
print("fruits type: ",type(fruits)) 

print(" index 1 elem:-", fruits[1])

print("length or fruits: ", len(fruits))


lastIndex = len(fruits)-1
print(" last element index:", lastIndex, " value:", fruits[lastIndex] )



print()


print("-------------------------------dict")


car = {
  "name": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["blue", "red"],
  "address": {
    "city": "blr",
    "area":"begur",
    "state": "ka"
  }
}

print("car", car)

print("type of car", type(car))

print("car name",car['name']) # to access speific property

print("len ", len(car))

