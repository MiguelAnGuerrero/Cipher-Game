# Basic Number Cipher
# Just translates ASCII

def convertTo():
    word = input()
    numbers = [ord(c) for c in word]
    print(numbers)
charAscii = input("Map the numbers to the letter: \n\n[99, 97, 116]\n\n")
charAscii = charAscii.upper()
if(charAscii == "CAT"):
    print("You unlock the compute, Good job!")
else:
    print("Please try again!")

if __name__ == "__main__":
    convertTo()