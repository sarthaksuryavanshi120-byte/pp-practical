n = int(input("Enter the size of array: "))
arr = []

for i in range(n):
    val = int(input("Enter the number: "))
    arr.append(val)

# sort only once after taking all inputs
arr.sort()
print("Sorted array:", arr)

target = int(input("Enter the target: "))

s = 0
e = n - 1

while s <= e:
    mid = (s + e) // 2

    if arr[mid] == target:
        print("Target found at index", mid)
        break

    elif arr[mid] > target:
        e = mid - 1

    else:
        s = mid + 1
else:
    print("Target not found")
