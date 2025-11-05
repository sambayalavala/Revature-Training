#Convert CamelCase to snake_case
string = input("Enter a CamelCase string: ")
result = ""

for char in string:
    if char.isupper():
        if result != "":
            result += "_"
        result += char.lower()
    else:
        result += char

print("snake_case string:", result)



