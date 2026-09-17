import math
p = 7
q = 11
seed = 16
num_bits = 5
n = p * q
if math.gcd(seed, n) != 1:
    print("Invalid Seed")
else:
    x = seed
    bits = []
    print("Blum Blum Shub Generator")
    print("------------------------")
    for i in range(num_bits):
        x = (x * x) % n
        bit = x % 2
        bits.append(bit)
        print("Random Number =", x, " Output Bit =", bit)
print("\nBit Stream =", ''.join(map(str, bits)))
