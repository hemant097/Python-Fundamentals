import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# print(chars)

chars = list(chars)
key = chars.copy() #if we do key=chars, any changes made in key will reflect in chars, as both will refer to same list, thus we are copying here
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

#we are getting the index of each character of the plain_text from chars[], and appending the corresponding index's value from key[]
for letter in plain_text:
    index = chars.index(letter)
    cipher_text+=key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#Decryption

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+=chars[index]

print(f"user given encrypted message: {cipher_text}")
print(f"decrypted message: {plain_text}")


