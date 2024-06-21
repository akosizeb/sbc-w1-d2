from random import randint

num1 = int(input("ENTER FIRST NUMBER: "))
num2 = int(input("ENTER SECOND NUMBER: "))
num3 = int(input("ENTER THIRD NUMBER: "))

p1 = randint(1,2)
p2 = randint(1,2)
p3 = randint(1,2)

user = f"{num1} {num2} {num3}"
result = f"{p1} {p2} {p3}"

print(f"PUSTA: {user}")
print(f"RESULTA: {result}")

if num1 == p1 and num2 == p2 and num3 == p3:
    print("Naysss Daog Ka!")

elif (num1 == p1 and num2 == p3 and num3 == p2) or (num1 == p2 and num2 == p1 and num3 == p3) or (num1 == p2 and num2 == p3 and num3 == p1) or (num1 == p3 and num2 == p1 and num3 == p2) or (num1 == p3 and num2 == p2 and num3 == p1):
    print("Nayss Daog kas Rambol! ")

else:
    print("Toinks Pilde Ka!")