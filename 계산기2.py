a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
c = input("Input between +, -, *, / and % : ")

d = 0
if c == "+":
    d = a - b
elif c == "-":
    d = a - b
elif c == "*":
    d = a * b
elif c == "/":
    d = a / b
elif c == "%":
    d = a % b
else:
    print("error")

print(d)
