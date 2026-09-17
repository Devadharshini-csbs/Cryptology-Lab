print("==============================================")
print(" MODULAR ARITHMETIC CALCULATOR")
print("==============================================")
a = int(input("Enter the First Integer (a): "))
b = int(input("Enter the Second Integer (b): "))
m = int(input("Enter the Modulus (m): "))
if m <= 0:
    print("Modulus must be greater than 0.")
else:
    while True:
        print("\n========== MENU ==========")
        print("1. Modular Addition")
        print("2. Modular Subtraction")
        print("3. Modular Multiplication")
        print("4. Modular Exponentiation")
        print("5. Exit")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            result = (a + b) % m
            print("\nModular Addition")
            print(f"({a} + {b}) mod {m} = {result}")
        elif choice == 2:
            result = (a - b) % m
            print("\nModular Subtraction")
            print(f"({a} - {b}) mod {m} = {result}")
        elif choice == 3:
            result = (a * b) % m
            print("\nModular Multiplication")
            print(f"({a} × {b}) mod {m} = {result}")
        elif choice == 4:
            result = pow(a, b, m)
            print("\nModular Exponentiation")
            print(f"({a}^{b}) mod {m} = {result}")
        elif choice == 5:
            print("\nExiting the Program...")
            break
        else:
            print("\n Invalid choice ! Please select between 1 and 5. ")

