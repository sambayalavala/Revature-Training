 # Concatenate Characters of userchoices and display error message if not possible
string=input("Enter a string:")
start1=int(input("Enter a start number:"))
end1=int(input("Enter a end number:"))

start2=int(input("Enter a start number:"))
end2=int(input("Enter a end number:"))

if start1<=0 or end1>len(string) or start1 >=end1 or start2 <= 0 or end2 > len(string) or start2 >= end2:
    print("Error not possible")
else:
    part1=string[start1:end1]
    part2=string[start2:end2]
    result=part1+part2
    print('Concatenate Characters :',result)



