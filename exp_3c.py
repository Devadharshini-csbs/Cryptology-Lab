import numpy as np
key=np.array([[3,3],[2,5]])
inverse=np.array([[15,17],[20,9]])
def process(text):
    text=text.upper()
    if len(text)%2!=0:
        text+="X"
    return text
def convert(text):
    return [ord(i)-65 for i in text]
def encrypt(text):
    text=process(text)
    nums=convert(text)
    cipher=""
    for i in range(0,len(nums),2):
        pair=np.array([[nums[i]],[nums[i+1]]])
        result=np.dot(key,pair)%26
        cipher+=chr(result[0][0]+65)
        cipher+=chr(result[1][0]+65)
    return cipher
def decrypt(cipher):
    nums=convert(cipher)
    plain=""
    for i in range(0,len(nums),2):
        pair=np.array([[nums[i]],[nums[i+1]]])
        result=np.dot(inverse,pair)%26
        plain+=chr(result[0][0]+65)
        plain+=chr(result[1][0]+65)
    return plain
plain=input("Enter Plaintext : ")
cipher=encrypt(plain)
print("Ciphertext :",cipher)
print("Decrypted :",decrypt(cipher))
