from string import ascii_uppercase
def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key + ascii_uppercase:
        if ch == 'J':
            continue
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'

    for i, row in enumerate(matrix):
        if ch in row:
            return i, row.index(ch)

def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + "X"
            i += 1

    return result

def encrypt(text, matrix):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def decrypt(cipher, matrix):
    plain = ""

    for i in range(0, len(cipher), 2):
        a = cipher[i]
        b = cipher[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]
        else:
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]
    cleaned = ""
    i = 0
    while i < len(plain):
        if i + 2 < len(plain) and plain[i] == plain[i + 2] and plain[i + 1] == 'X':
            cleaned += plain[i]
            i += 2
        else:
            cleaned += plain[i]
            i += 1
    if cleaned.endswith('X'):
        cleaned = cleaned[:-1]

    return cleaned

key = input("Enter Keyword : ")
plain = input("Enter Plaintext : ")

matrix = generate_key_matrix(key)

print("\nKey Matrix")
for row in matrix:
    print(" ".join(row))
cipher = encrypt(plain, matrix)
print("\nCiphertext :", cipher)
original = decrypt(cipher, matrix)
print("Decrypted Text :", original)
