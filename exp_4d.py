import hashlib
message=input("Enter Message: ")
hash_value=hashlib.sha1(message.encode())
print("SHA-1 Digest:",hash_value.hexdigest())
