# Function with POSITIONAL arguments
def add(a, b):        # a and b must be given in order
    return a + b

# Function with KEYWORD arguments
def greet(first, last):   # arguments can be given using names
    return "Hello, " + first + " " + last

# Function with DEFAULT argument
def power(base, exp=2):   # exp has default value = 2
    return base ** exp

# Function with VARIABLE-LENGTH arguments (*args)
def multiply(*nums):      # *nums collects many values
    result = 1
    for n in nums:
        result *= n
    return result

# Function with VARIABLE-LENGTH keyword arguments (**kwargs)
def person(**info):       # **info collects key=value pairs
    return info

# Calling the functions
print("Sum:", add(5, 10))                          # positional
print(greet(first="John", last="Doe"))             # keyword
print("Square:", power(5))                         # default
print("Cube:", power(5, 3))                        # default changed
print("Product:", multiply(2, 3, 4))               # *args
print("Person:", person(name="Alice", age=30))     # **kwargs
