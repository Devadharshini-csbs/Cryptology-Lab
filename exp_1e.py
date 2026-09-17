import math
a = int(input("Enter the value of a: "))
n = int(input("Enter the value of n: "))
phi = 0
for i in range(1, n + 1):
    if math.gcd(i, n) == 1:
        phi += 1
print("\nEuler's Totient Function")
print("φ(", n, ") =", phi)
if math.gcd(a, n) == 1:
        print(a, "and", n, "are coprime.")
        result = pow(a, phi, n)
        print("\nEuler's Theorem Verification")
        print(f"{a}^{phi} mod {n} = {result}")
        if result == 1:
            print("Euler's Theorem is Verified.")
        else:
            print("Euler's Theorem is NOT Verified.")
else:
    print(a, "and", n, "are not coprime.")
    print("Euler's Theorem cannot be applied.")
