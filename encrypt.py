#!/usr/bin/env python

from maps import letters_to_numbers, numbers_to_letters,uppercase_letters_to_numbers,uppercase_numbers_to_letters

def encrypt(plaintext, shift=0):
    """
    Uses the Caesar cipher to encrypt a plaintext message.
    :param plaintext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    #create an empty string to store encrypted text
    encrypted_string = ""
    # loop through plaintext look at eache letter in order
    for letter in plaintext:
        if letter not in letters_to_numbers:
            encrypted_string += letter
            continue 
        #look up the numeric representation for the letter (use dictionary)
        unshifted_letter = letters_to_numbers[letter]
        #add the shift to the numeric representation
        shifted_index = unshifted_letter + shift
        if shifted_index > 26:
            shifted_index -= 26
        #look up the letter associated with the shifted index(use other dictonary)
        shifted_letter = numbers_to_letters[shifted_index]
        #add shifted letter to encrypted string
        encrypted_string += shifted_letter
    #return the encrypted string
    return encrypted_string


if __name__ == "__main__":
    plaintext = input("Message to encrypt: ")
    shift = int(input("Shift: "))
    print(encrypt(plaintext, shift))
