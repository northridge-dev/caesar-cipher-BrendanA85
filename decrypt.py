#!/usr/bin/env python

from maps import uppercase_letters_to_numbers,uppercase_numbers_to_letters
letters_to_numbers = {
    'a': 1, 'b' : 2, 'c' : 3, 'd':4,'e':5,'f':6,'g':7,'h':8, 'i':9,'j':10,'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
}
numbers_to_letters = {}
for letter, number in letters_to_numbers.items():
    numbers_to_letters[number] = letter

def decrypt(ciphertext, shift=0):
    """
    Decrypts a Caesar cipher encrypted message.
    :param ciphertext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    decrypted_string = ""
    for letter in ciphertext:
        if letter not in letters_to_numbers:
            decrypted_string += letter
            continue
        shifted_letter = letters_to_numbers[letter]
        unshifted_index = shifted_letter - shift
        if unshifted_index < 1:
            unshifted_index += 26
        unshifted_letter = numbers_to_letters[unshifted_index]
        decrypted_string += unshifted_letter
    return decrypted_string


if __name__ == "__main__":
    ciphertext = input("Message to decrypt: ")
    shift = int(input("Shift: "))
    print(decrypt(ciphertext, shift))
