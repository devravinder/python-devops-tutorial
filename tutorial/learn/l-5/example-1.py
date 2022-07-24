
"""
pring even numbers till the given number
"""

def pring_even(given):
    for num in range(0, given, 1):
        if(num % 2 ==0):
          print(num)
    print("------------------done")
"""
    print(" another way")
        for num in range(0, given, 2):
            print(num)
"""
  

pring_even(10)


pring_even(20)