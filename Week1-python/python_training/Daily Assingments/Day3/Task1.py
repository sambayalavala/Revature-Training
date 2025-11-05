# Split String into Equal Parts
string1=input("Enter a string:")
num=int(input("Enter anumber:"))

if len(string1) % num !=0:
    print("Error! it not possible of equal parts")
else:
    equal_parts=len(string1) // num
    for i in range(0,len(string1),equal_parts):
        print(string1[i:i+equal_parts])