letters_to_numbers = {
    'a': 1, 'b' : 2, 'c' : 3, 'd':4,'e':5,'f':6,'g':7,'h':8, 'i':9,'j':10,'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
}
numbers_to_letters = {}
for letter, number in letters_to_numbers.items():
    numbers_to_letters[number] = letter

uppercase_letters_to_numbers = {}
uppercase_numbers_to_letters = {}
for letter, number in letters_to_numbers.items():
    uppercase = letter.upper()
    uppercase_letters_to_numbers[uppercase] = number
    uppercase_numbers_to_letters[number] = uppercase
