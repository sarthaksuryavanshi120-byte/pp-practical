n = int(input("Enter the size of list"))

number = []
 
for i in range(n):
    val = int(input("Enter the number"))
    number.append(val) 

squares = list(map(lambda x:x*x,number))
evens = list(filter(lambda x:x%2 == 0,number ))    

print("squares",squares)
print("even",evens)

squares_lc = [x*x for x in number]
even_lc = [x for x in number if x%2 == 0]

print(squares_lc)
print(even_lc)