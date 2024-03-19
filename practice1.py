num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the limit: "))

m = [a for a in range(num3) if a % num1 == 0 or a % num2 == 0]

s = sum(m)

print(f"The sum of multiples of {num1} or {num2} up to {num3} is {s}")