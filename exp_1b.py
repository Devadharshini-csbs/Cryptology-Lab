#Secure Communication Key Validation using Euclidean Algorithm
def find_gcd(a, b):
    if a < b:
        a, b = b, a
    print("\nSteps of Euclidean Algorithm:")
    while b != 0:
        remainder = a % b
        print(f"{a} ÷ {b} = Quotient {a//b}, Remainder {remainder}")
        a = b
        b = remainder
    return a
print("=== Secure Communication Key Validation ===")
parameter1 = int(input("Enter the first encryption parameter: "))
parameter2 = int(input("Enter the second encryption parameter:"))
gcd = find_gcd(parameter1, parameter2)
print("\nGreatest Common Divisor (GCD) =", gcd)

if gcd == 1:
    print("\nThe encryption parameters are COPRIME.")
    print("Secure communication can be established.")
else:
    print("\nThe encryption parameters are NOT COPRIME.")
    print("Communication setup rejected.")
    print("Choose different encryption parameters.")
