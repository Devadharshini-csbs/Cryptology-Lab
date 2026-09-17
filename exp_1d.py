print("===========================================")
print(" RSA Prime Validation using Fermat's Test ")
print("===========================================")
a = int(input("Enter the value of a: "))
p = int(input("Enter the candidate prime number (p): "))

if p <= 1:
    print("\nInvalid Input!")
    print("The candidate number p must be greater than 1.")
else:
    result = pow(a, p-1, p)
    print("\nResult of Fermat Test")
    print(f"({a}^{p-1}) mod {p} = {result}")
if result == 1:
    print("\nThe number satisfies Fermat's Little Theorem.")
    print("It is a probable prime.")
    print("Candidate is suitable for further RSA key generation.")
else:
    print("\nThe number does not satisfy Fermat's Little Theorem.")
    print("It is composite.")
    print("Candidate is NOT suitable for RSA key generation.")
