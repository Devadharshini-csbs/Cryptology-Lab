def encrypt(text, shift):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch)-65+shift)%26+65)
        else:
            result += ch
        return result
def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch)-65-shift)%26+65)
        else:
            result += ch
    return result

plain = input("Enter Plaintext : ")
shift = int(input("Enter Key : "))
cipher = encrypt(plain, shift)
print("Ciphertext :", cipher)
original = decrypt(cipher, shift)
print("Decrypted :", original)
