#Vigenere cipher

def letter_to_number(letter):
    return ord(letter) - 65


def cipher(plaintext, key, t):
    # Todo mayus y sin espacios inicialmente
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    # Cada letra se cifra sumando su orden, en la matriz, la letra en i,j es la letra i+j%26 
    ciphertext = ""
    for i in range(len(plaintext)):
        c = letter_to_number(plaintext[i]) + letter_to_number(key[i % len(key)])

        ciphertext += chr(c % 26 + 65)
        # Un espacio cada t letras
        if (i + 1) % t == 0:
            ciphertext += " "


    return ciphertext


def uncipher(ciphertext, key):
    #Todo mayus y sin espacios inicialmente
    ciphertext = ciphertext.upper()
    key = key.upper().replace(" ", "")
    # Cada letra se descifra, si es un espacio, solo se copia
    plaintext = ""
    j = 0
    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
            continue
        c = letter_to_number(ciphertext[i]) - letter_to_number(key[j % len(key)])
        j += 1

        plaintext += chr(c % 26 + 65)

    return plaintext



while True:
    option = input("Ingrese 0 para encriptar o 1 para desencriptar: ")
    if option == "0":
        plaintext = input("Ingrese el texto a encriptar: ")
        key = input("Ingrese la clave: ")
        length = int(input("Ingrese la longitud de los bloques(t): "))
        ciphertext = cipher(plaintext, key, length)
        print("Texto encriptado:\n" + ciphertext + "\n")
    elif option == "1":
        ciphertext = input("Ingrese el texto a desencriptar: ")
        key = input("Ingrese la clave: ")
        plaintext = uncipher(ciphertext, key)
        print("Texto desencriptado:\n" + plaintext + "\n")
    else:
        print("Opción inválida. Por favor ingrese 0 o 1.")

# TO BE OR NOT TO BE THAT IS THE QUESTION
# KSMEHZ BBLKS MEMPO GAJXS EJCSF LZSY
# THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME
# VYCG XWU RQT VFG KNP LGC XCQ XVK EBI ASR ZAI NFG WPP FS