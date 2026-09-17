from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key = b'12345678'
cipher = DES.new(key, DES.MODE_ECB)

plaintext = input("Enter Plaintext: ")

ciphertext = cipher.encrypt(
    pad(plaintext.encode(), DES.block_size)
)
print("Encrypted Data:", ciphertext.hex())
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(
    decipher.decrypt(ciphertext),
    DES.block_size
)
print("Decrypted Data:", decrypted.decode())
