# Homophonic cipher
import random

KEY = {
    'A': [9, 12, 33, 47, 53, 67, 78, 92],
    'B': [48, 81],
    'C': [13, 41, 62],
    'D': [1, 3, 45, 79],
    'E': [14, 16, 24, 44, 46, 55, 57, 64, 74, 82, 87, 98],
    'F': [10, 31],
    'G': [6, 25],
    'H': [23, 39, 50, 56, 65, 68],
    'I': [32, 70, 73, 83, 88, 93],
    'J': [15],
    'K': [4],
    'L': [26, 37, 51, 84],
    'M': [22, 27],
    'N': [18, 58, 59, 66, 71, 91],
    'O': [0, 5, 7, 54, 72, 90, 99],
    'P': [38, 95],
    'Q': [94],
    'R': [29, 35, 40, 42, 77, 80],
    'S': [11, 19, 36, 76, 86, 96],
    'T': [17, 20, 30, 43, 49, 69, 75, 85, 97],
    'U': [8, 61, 63],
    'V': [34],
    'W': [60, 89],
    'X': [28],
    'Y': [21, 52],
    'Z': [2]
}

# Diccionario inverso para desencriptar
INVERSE_KEY = {num: char for char, nums in KEY.items() for num in nums}


def cipher(plaintext):
    # Todo mayus y sin espacios inicialmente
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = []
    for char in plaintext:
        if char in KEY:
            ciphertext.append(str(random.choice(KEY[char])))
    return " ".join(ciphertext)


def uncipher(ciphertext):
    # Separar los números por espacios o comas
    numbers = ciphertext.replace(",", " ").split()
    plaintext = ""
    for num in numbers:
        if num.isdigit() and int(num) in INVERSE_KEY:
            plaintext += INVERSE_KEY[int(num)]
        else:
            plaintext += "?"
    return plaintext

def main():
    while True:
        option = input("Ingrese 0 para encriptar o 1 para desencriptar: ")
        if option == "0":
            plaintext = input("Ingrese el texto a encriptar: ")
            ciphertext = cipher(plaintext)
            print("Texto encriptado:\n" + ciphertext + "\n")
        elif option == "1":
            ciphertext = input("Ingrese el texto a desencriptar: ")
            plaintext = uncipher(ciphertext)
            print("Texto desencriptado:\n" + plaintext + "\n")
        else:
            print("Opción inválida. Por favor ingrese 0 o 1.")


main()
# Crypto is fun
# 13 5 26 0 22 81 88 47
# 62 40 21 95 69 90 32 19 31 61 91
