"""
match / switch
"""


from email.policy import default


x = 0

match x:
    case 0:
        print("zero")
    case 1:
        print("one")
    case default:
        print(" morethan one")
