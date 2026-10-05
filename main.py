# Calculator:
num1=int(float(input("Enter first number:")))
operator=input("Enter operator:")
num2=int(float(input("Enter second number:")))
if operator =="+":
    print(num1 + num2)
elif operator =="-":
    print(num1 - num2)
elif operator =="*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator =="//":
    print(num1 // num2)
elif operator =="**":
    print(num1 ** num2)
else:
    print("Invalid!:Operator")
