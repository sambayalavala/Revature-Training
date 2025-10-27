num = int(input("Enter number :"))
original = num
digits = len(str(num))
armostrong_s = 0
while num > 0:
    digit = num % 10
    armostrong_s += digit ** digits
    num = num // 10
if armostrong_s == original:
    print(original, "it is a armstrong")
else:
    print(original, "it is not armstrong")


