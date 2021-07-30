def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for l in plaintext:
        i = (alphabet.index(l) + key) % 26
        result =result + alphabet[i]

    return result


def decrypt(cipher, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for l in cipher:
        i = (alphabet.index(l) - key) % 26
        result += alphabet[i]

    return result


Text = input("Enter text to be encrypted: ")
key = int(input("Enter the Key: "))
ciphertext = encrypt(Text, key)
print("Encypted Text: ", ciphertext)
plaintext = decrypt(ciphertext, key)
print("Decryped Text: ", plaintext)