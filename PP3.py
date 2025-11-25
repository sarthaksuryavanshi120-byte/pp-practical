
# Print prime numbers in a range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers are: ", end="")
for n in range(start, end + 1):
    if n < 2:
        continue

    prime = True
    for j in range(2, n):
        if n % j == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")
