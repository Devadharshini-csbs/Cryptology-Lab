# Linear Feedback Shift Register (LFSR)
register = [1,0,1,1]
n = 10
print("Linear Feedback Shift Register")
print("------------------------------")
for i in range(n):
    feedback = register[0] ^ register[3]
    output = register[-1]
    register = [feedback] + register[:-1]
    print("Step", i+1)
    print("Feedback =", feedback)
    print("Output =", output)
    print("Register =", register)
    print()
