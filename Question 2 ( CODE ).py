print("----- SIMPLE CALCULATOR -----")
print("\nChoose an option:")
print("1. Arithmetic Operations")
print("2. Comparison Operations")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
while True : # loop ke bina bhi ho sakta hai but i wanted repeated so used loops
  choice = int(input("\nEnter your choice (1-4): "))

  match choice:
    case 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nArithmetic Operations")
        print("Addition =", num1 + num2)
        print("Subtraction =", num1 - num2)
        print("Multiplication =", num1 * num2)
        print("Division =", num1 / num2)
        print("Modulus =", num1 % num2)
        print("Power =", num1 ** num2)

    # Comparison Operations
    case 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nComparison Operations")
        print("num1 > num2 =", num1 > num2)
        print("num1 < num2 =", num1 < num2)
        print("num1 == num2 =", num1 == num2)
        print("num1 != num2 =", num1 != num2)

    # Celsius to Fahrenheit
    case 3:
        celsius = float(input("Enter temperature in Celsius: "))

        fahrenheit = (celsius * 9/5) + 32

        print("Temperature in Fahrenheit =", fahrenheit)

    # Fahrenheit to Celsius
    case 4:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        celsius = (fahrenheit - 32) * 5/9

        print("Temperature in Celsius =", celsius)

    # Invalid choice or Exit
    case _:
        print("Invalid choice! Please select between 1 and 4.")

# output
# Choose an option:
# 1. Arithmetic Operations
# 2. Comparison Operations
# 3. Celsius to Fahrenheit
# 4. Fahrenheit to Celsius

# Enter your choice (1-4): 1
# Enter first number: 4
# Enter second number: 6

# Arithmetic Operations
# Addition = 10.0
# Subtraction = -2.0
# Multiplication = 24.0
# Division = 0.6666666666666666
# Modulus = 4.0
# Power = 4096.0

# Enter your choice (1-4): 2
# Enter first number: 3
# Enter second number: 4

# Comparison Operations
# num1 > num2 = False
# num1 < num2 = True
# num1 == num2 = False
# num1 != num2 = True