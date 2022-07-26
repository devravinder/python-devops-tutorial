"""

control statement:-

---loops

for 
while

"""
fruits = ["apple", "banana", "cherry", "dragon"]

for f in fruits:
    print(f)

print("===================")

employees = [
    {"name": "ravinder", "role": "dev"},
    {"name": "srinivas", "role": "manager"},
    {"name": "girish", "role": "chairmen"},
    {"name": "kishore", "role": "technical manager"},
    {"name": "Muthu", "role": "dev"},
]

print("employees---")
for f in employees:
    print(f)

print("------------------------")

for f in employees:
    # print(f)
    f["empId"] = 1

print("------------------------")

for f in employees:
    print(f)

print()

print(" iterating over dist / looping over dist")

ec2 = {"name": "dev-server", "tags": ["dev", "server", "us-east"], "region": "us-east"}
print("ec2", ec2)
for key in ec2:
    print("key: ", key, "value: ", ec2[key])  ## ec2["name"]


print("======= below topics are not imp ============")


name = "ragu rama raju"
for char in name:
    print(char)


print()
print(" range (10)-------------")
for num in range(10):  # like an array [0, 1,2 ....till 9] ( 10 not included)
    print(num)


print()
print(" range (2,10) (from, to)-------------")
for num in range(2, 10):
    print(num)

print()
print(" range (2,10, 2) ( from, to, increamnet)-------------")
for num in range(2, 10, 2):
    print(num)


print("=============== for continue =============")


print(" range reverse-------------")
for num in range(10, 0, -1):
    print(num)
