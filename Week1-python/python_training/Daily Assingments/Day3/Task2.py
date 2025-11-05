# :Remove Duplicates from String
string=input("Enter a string:")
result=''
for char in string:
    if char not in result:
        result +=char
print(result)