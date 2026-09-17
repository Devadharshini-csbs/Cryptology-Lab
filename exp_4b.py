def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def mod_inverse(e,phi):
    for d in range(1,phi):
        if (e*d)%phi==1:
            return d
p=17
q=11
n=p*q
phi=(p-1)*(q-1)
e=7
d=mod_inverse(e,phi)
print("Public Key:",(e,n))
print("Private Key:",(d,n))
message=int(input("Enter Message (<187): "))
cipher=pow(message,e,n)
print("Encrypted Message:",cipher)
plain=pow(cipher,d,n)
print("Decrypted Message:",plain)
