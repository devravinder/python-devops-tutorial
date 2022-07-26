"""
ref: https://www.w3schools.com/python/python_operators.asp

Operators:-



Imp:-
Arithmetic: +, -, *, /, %
comparision: ==, !=, <, <=, >, >=,


less imp:-
logical: and, or, not 
Membership: in



"""
print("----------------------")
x = 3
y = 2
z = x + y
print(z)

z = x - y
print(z)

z = x * y
print(z)


z = x / y  # this is standard
print(z, " float division type ", type(z))


z = x // y  # 1.5 -> 1
print(z, " normal  division ( // ) type ", type(z))


print("---------------------------------")

balance = 200

withdraw = 150

isAllowed = balance > withdraw  # result is boolean

print("isAllowed", isAllowed)

isSame = balance == withdraw  # result is boolean

print("isSame", isSame)


isNotSame = balance != withdraw  # result is boolean ( not imp )

print("isNotSame", isNotSame)


car1 = {
    "name": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["blue", "red"],
    "address": {"city": "blr", "area": "begur", "state": "ka"},
}

car2 = {
    "name": "Ford",
    "model": "Mustang",
    "year": 1964,
    "address": {"city": "blr", "area": "begur", "state": "ka"},
}

print()
print("-----------in operator")
print("colors" in car1)
result2 = "colors" in car2  ## general usage # holding result in a variable
print("colors" in car2)
print("res2: ", result2)
