import hashlib
message = input("Enter Message: ")
hash_value = hashlib.md5(message.encode())
print("MD5 Digest:", hash_value.hexdigest())
