n = int(input("Enter the size of array: "))

arr = []
for i in range(n):
    val = int(input("Enter number: "))
    arr.append(val)

target = int(input("Enter the target: "))
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found in the list")
