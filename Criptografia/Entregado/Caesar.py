
def shift(char, k):
    # Si es una letra, desplazarla, si no (un espacio), devolverla normal
    if char.isalpha():
        char = char.upper()
        shifted = (ord(char) - ord('A') + k) % 26 + ord('A')
        return chr(shifted)
    return char



def encrypt(plaintext, k, length):
    # Asegurarse de que el texto plano esté en mayúsculas y sin espacios
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    #Recorrer cada caracter, desplazarlo, agregar espacio cada 5 caracteres
    i = 0
    for char in plaintext:
        ciphertext += shift(char, k)
        if i % length == 0 and i != 0:
            ciphertext += " "
        i += 1
    return ciphertext



def decrypt(ciphertext, k):
    plaintext = ""
    #Recorrer cada caracter, desplazarlo en sentido contrario
    for char in ciphertext:
        plaintext += shift(char, -k)
    return plaintext


while True:
    option = input("Ingrese 0 para encriptar o 1 para desencriptar: ")
    if option == "0":
        plaintext = input("Ingrese el texto a encriptar: ")
        k = int(input("Ingrese el valor de desplazamiento (k): "))
        length = int(input("Ingrese la longitud de los bloques: "))
        ciphertext = encrypt(plaintext, k, length)
        print("Texto encriptado:\n" + ciphertext + "\n")
    elif option == "1":
        ciphertext = input("Ingrese el texto a desencriptar: ")
        k = int(input("Ingrese el valor de desplazamiento (k): "))
        plaintext = decrypt(ciphertext, k)
        print("Texto desencriptado:\n" + plaintext + "\n")
    else:
        print("Opción inválida. Por favor ingrese 0 o 1.")


# WKLVL VHAWU HPHOB LQVHF XUHHQ FUBSW LRQGR QRWXV HLWWR SURWH FWYDO XDEOH LQIRU PDWLR Q

# LWLVF ODLPH GWKHH DUOLH VWNQR ZQUHI HUHQF HWRWK LVWBS HRIFL SKHUL VLQWK HNDPD VXWUD ZKLFK VDBVZ RPHQV KRXOG OHDUQ WKHDU WRIVH FUHWZ ULWLQ JWRFR QFHDO WKHLU OLDVR QV

# RETURN TO ROME