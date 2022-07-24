"""
pring 3 multiples till 100

"""

for num in range(0, 100, 1):
    if(num%3==0):
        print(num)
  
print(" another way")

for num in range(0, 100, 3):
        print(num)
  
print("===================================")


"""
print i to j, with an increament by k
i.e -> if i=1,  j=100, and k = 1 

"""

print()

for n in range(1,100,1):
 print(n)



print("===========================")
# i.e -> if i=100,  j=50, and k = -2


for n in range(100,50,-2):
 print(n)


print("----------------best way")

i = 100
j = 50
k = -2

for n in range(i, j, k):
 print(n)