# File Manipulation Program

# 1. Write data to a file
with open("sample.txt", "w") as file1:
    file1.write("This is the first line.\n")
    file1.write("Python file handling is interesting!\n")

# 2. Read data from the file
with open("sample.txt", "r") as file1:
    print("Contents of sample.txt after writing:")
    print(file1.read())

# 3. Append data to the file
with open("sample.txt", "a") as file1:
    file1.write("Appending a new line to the file.\n")

# 4. Read data again to verify append
with open("sample.txt", "r") as file1:
    print("\nContents of sample.txt after appending:")
    print(file1.read())

# 5. Copy contents from one file to another
with open("sample.txt", "r") as source, open("copy_sample.txt", "w") as destination:
    for line in source:
        destination.write(line)

# 6. Display copied file contents
with open("copy_sample.txt", "r") as destination:
    print("\nContents of copy_sample.txt (copied file):")
    print(destination.read())
