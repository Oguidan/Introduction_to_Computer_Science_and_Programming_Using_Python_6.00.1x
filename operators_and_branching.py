# This file will show how to use operators and branching in python

2 < 3
# Output True, because 2 is less than 3

2.0 > 3.0
# Output False, because 2.0 is not greater than 3.0

2 <= 2
# Output True, because 2 is less than or equal to 2

2 < 2
# Output False, because 2 is not less than 2

2 == 2
# Output True, because 2 is equal to 2

# A simple example
x = int(input("Enter an integer: "))
if x % 2 == 0:
    print("")
    print("Even")
else:
    print("")
    print("Odd")
print("Done with conditional")

# NESTED CONDITIONALS
if x % 2 == 0:
    if x % 3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divible by 2 and not by 3")
elif x % 3 == 0:
    print("Divisible by 3 and not by 2")

# INDENTATION
xx = float(input("Enter a number for xx: "))
y = float(input("Enter a number for y: "))
if xx == y:
    print("xx and y are eaqual")
    if y != 0:
        print("therefore, xx/y is", xx / y)
elif xx < y:
    print("xx is smaller")
else:
    print("y is smaller")
print("thanks!")