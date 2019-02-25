# author: Luke Johnson
#
# Program simulates Vigenere Cipher by encoding and decoding messages using the a Vigenere Square and a key
#

# Function creates the vigenere square
def vigenere_square():
    square = []
    alphabet = [chr(i).upper() for i in range(97, 123)]
    square.append([i for i in alphabet])

    #print('Plain: ', end='')
    # for letter in alphabet:
    #     print('{:>3}'.format(letter), end='')
    # print()

    for row in range(1, len(alphabet)):
        # print('{:<7}'.format(row), end='')
        i = row
        iteration = 0
        square.append([])

        while iteration < len(alphabet):
            if i == len(alphabet):
                i = 0
            square[row].append(alphabet[i])
           # print('{:>3}'.format(alphabet[i]), end='')
            iteration += 1
            i += 1
    # for i in square:
    #      print(i)
    return square


# Function to generate a list of characters for the enciphered message or plaintext message, and the key
def get_key_and_text_list(plaintext, key):
    text_list = [i for i in plaintext]

    # generate key list
    key_list = []
    iteration = 0
    index = 0
    while iteration < len(text_list):
        if index == len(key):
            index = 0
        key_list.append(key[index])
        iteration += 1
        index += 1

    return text_list, key_list


# Function enciphers a message
def encipher(plaintext, key):
    square = vigenere_square()
    row = None
    column = None

    # generate list of plaintext and key
    text_list, key_list = get_key_and_text_list(plaintext, key)
    enciphered_list = []
    # print(text_list)
    # print(key_list)

    for index in range(len(text_list)):
        plain_letter = text_list[index]
        key_letter = key_list[index]

        for i in range(len(square)):
            if square[i][0] == key_letter:
                row = i
                # print(row)
                break

        for i in square[0]:
            if i == plain_letter:
                column = square[0].index(i)
                # print(column)
                break
        enciphered_letter = square[row][column]
        enciphered_list.append(enciphered_letter)
    message = list_to_string(enciphered_list)

    return message



# Function deciphers a message
def decipher(encrypted_text, key):
    square = vigenere_square()
    row = None
    column = None

    encrypted_text_list, key_list = get_key_and_text_list(encrypted_text, key)
    plain_text_list = []

    for index in range(len(encrypted_text_list)):
        encrypted_letter = encrypted_text_list[index]
        key_letter = key_list[index]

        for i in range(len(square)):
            if square[i][0] == key_letter:
                row = i
                # print(row)
                # print(square[row])
                break

        for i in square[0]:
            if i == encrypted_letter:
                column = square[row].index(i)
                # print(column)
                break
        plain_text_letter = square[0][column]
        plain_text_list.append(plain_text_letter)
    # print(plain_text_list)
    message = list_to_string(plain_text_list)

    return message


# function converts a list to a string
def list_to_string(list):
    string = ''
    for i in list:
        string += i
    return string


# def main():
#     plaintext = input('Enter a message').upper()
#     key = input('Enter the key').upper()
#     enciphered_list = encipher(plaintext, key)
#     deciphered_list = decipher(enciphered_list, key)
#     print('Original:', plaintext)
#     print('Enciphered', enciphered_list)
#     print('Deciphered:', deciphered_list)
#
# if __name__ == '__main__':
#     main()