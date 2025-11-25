import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Division = Error (cannot divide by zero)")
