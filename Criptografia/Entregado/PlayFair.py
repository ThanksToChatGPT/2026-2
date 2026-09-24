#playfair
def desencriptar(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "").replace("J", "I")  # reemplazar J por I y quitar espacios
    
    plaintext = ""
    for i in range(0, len(ciphertext)-1, 2):
        letra1 = ciphertext[i]
        letra2 = ciphertext[i + 1]
        # buscar posiciones en la matriz
        pos1 = [(i, j) for i in range(5) for j in range(5) if key_matrix[i][j] == letra1][0]
        pos2 = [(i, j) for i in range(5) for j in range(5) if key_matrix[i][j] == letra2][0]

        if pos1[0] == pos2[0]:  # misma fila
            plaintext += key_matrix[pos1[0]][(pos1[1] - 1) % 5]
            plaintext += key_matrix[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:  # misma columna
            plaintext += key_matrix[(pos1[0] - 1) % 5][pos1[1]]
            plaintext += key_matrix[(pos2[0] - 1) % 5][pos2[1]]

        else:  # ni misma fila ni misma columna
            plaintext += key_matrix[pos1[0]][pos2[1]]
            plaintext += key_matrix[pos2[0]][pos1[1]]

    return plaintext

def encriptar(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "").replace("J", "I")  # reemplazar J por I y quitar espacios
    
    text = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            text += plaintext[i] + 'X' + plaintext[i + 1]
        elif i + 1 < len(plaintext):
            text += plaintext[i] + plaintext[i + 1]
        else:
            text += plaintext[i]
            

    plaintext = text

    #longitud par
    if len(plaintext) % 2 != 0:
        plaintext += 'X'

    print("Texto plano:", plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext)-1, 2):
        letra1 = plaintext[i]
        letra2 = plaintext[i + 1]
        # buscar posiciones en la matriz
        pos1 = [(i, j) for i in range(5) for j in range(5) if key_matrix[i][j] == letra1][0]
        pos2 = [(i, j) for i in range(5) for j in range(5) if key_matrix[i][j] == letra2][0]

        if pos1[0] == pos2[0]:  # misma fila
            ciphertext += key_matrix[pos1[0]][(pos1[1] + 1) % 5]
            ciphertext += key_matrix[pos2[0]][(pos2[1] + 1) % 5]
        elif pos1[1] == pos2[1]:  # misma columna
            ciphertext += key_matrix[(pos1[0] + 1) % 5][pos1[1]]
            ciphertext += key_matrix[(pos2[0] + 1) % 5][pos2[1]]

        else:  # ni misma fila ni misma columna
            ciphertext += key_matrix[pos1[0]][pos2[1]]
            ciphertext += key_matrix[pos2[0]][pos1[1]]

    return ciphertext

def key_matrix_from_string(key_string):
    key_string = key_string.upper().replace("J", "I").replace(" ", "")  # reemplazar J por I y quitar espacios
    key_matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # sin J
    for char in key_string:
        if char in alphabet:
            alphabet = alphabet.replace(char, "")
            key_matrix.append(char)
    for char in alphabet:
        key_matrix.append(char)
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]



def programa():
    while(True):
        a = input("Ingrese 0 para encriptar o 1 para desencriptar: ")
        if a == "0":

            key_matrix = input("Ingrese el texto inicial de la matriz llave: ")
            key_matrix = key_matrix_from_string(key_matrix)
            plaintext = input("Ingrese el texto a encriptar: ")
            ciphertext = encriptar(plaintext, key_matrix)
            print("Texto encriptado:", ciphertext)
        elif a == "1":
            key_matrix = input("Ingrese el texto inicial de la matriz llave: ")
            key_matrix = key_matrix_from_string(key_matrix)
            ciphertext = input("Ingrese el texto a desencriptar: ")
            plaintext = desencriptar(ciphertext, key_matrix)
            print("Texto desencriptado:", plaintext)
        else:
            print("Opción no válida. Intente de nuevo.")


programa()
