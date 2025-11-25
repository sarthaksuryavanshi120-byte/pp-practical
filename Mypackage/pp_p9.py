f = open("sample.txt","w")
f.write("This is the first line\n")
f.close()

f = open("sample.txt","r")
print("after write")
print(f.read())
f.close()

f=open("sample.txt","a")
f.write("Appending new line")
f.close()

source = open("sample.txt","r")
destination=open("copy_sample.txt","W")
for line in source:
    destination.write(line)
source.close()
destination.close()    

