# Slice Characters of user choices and display error message if not possible
string=input("Enter a string:")
start=int(input("enter a number:"))
end=int(input("Enter a number:"))

if start <=0 or end>len(string) or start >=end:
    print("Error not  possible of slicing")
else:
    print(string[start:end])