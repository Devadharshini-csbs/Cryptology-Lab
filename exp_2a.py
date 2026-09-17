# Linear Congruential Generator (LCG)
seed = 3
a = 5
c = 2
m = 13
n = 5
sequence = [seed]
x = seed
print("Linear Congruential Generator")
print("------------------------------")
for i in range(1, n + 1):
    x = (a * x + c) % m
    sequence.append(x)
    print(f"X{i} = {x}")
print("\nGenerated Sequence:", sequence)
