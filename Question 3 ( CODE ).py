print("---**AREA CALCULATOR**---")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

choice = int(input("Enter your choice (1, 2, 3, 4): "))

if choice == 1:
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle =", area)

elif choice == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print("Area of Rectangle =", area)

elif choice == 3:
    side = float(input("Enter the side: "))
    area = side * side
    print("Area of Square =", area)

elif choice == 4:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid choice!")


    # output

#     ---**AREA CALCULATOR**---
# 1. Circle
# 2. Rectangle
# 3. Square
# 4. Triangle
# Enter your choice (1, 2, 3, 4): 2
# Enter the length: 5
# Enter the width: 3
# Area of Rectangle = 15.0
