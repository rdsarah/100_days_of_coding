


# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for char in original_text:
#         new_index = alphabet.index(char) + shift_amount
#         if new_index > (len(alphabet)-1):
#             new_index = new_index % len(alphabet)
#         new_text += alphabet[new_index]
#     print(f"Here is the encoded result {encrypted_text}")

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for char in original_text:
#         new_index = alphabet.index(char) - shift_amount
#         if new_index < 0:
#             new_index = new_index % len(alphabet)
#         new_text += alphabet[new_index]
#     print(f"Here is the encoded result {decrypted_text}")

# merging both into one function 

def caesar(original_text, shift_amount, en_or_de):
    new_text = ""
    if en_or_de=="decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            new_text += char
        else:
            new_index = alphabet.index(char) + shift_amount
            new_index %= len(alphabet)
            new_text += alphabet[new_index]
    print(f"Here is the {en_or_de}d result: {new_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
loop = True

while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if restart=="no":
        loop = False
        print("Goodbye")