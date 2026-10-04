import numpy as np
def letter_to_number(letter):
    return ord(letter) - 65

def number_to_letter(number):
    return chr(number + 65)

def EEA(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d_prime, x_prime, y_prime = EEA(b, a % b)
        q = a // b
        d, x, y = d_prime, y_prime, x_prime - q * y_prime
        return d, x, y

def mod_inverse(K, m):
    det = int(np.linalg.det(K)) % m
    d, x, y = EEA(det, m)
    if d != 1:
        raise ValueError("Matrix is not invertible modulo {}".format(m))
    else:
        adj_K = np.array([[K[1][1], -K[0][1]], [-K[1][0], K[0][0]]])
        K_inv = (x * adj_K) % m
        return K_inv

def cipher(plaintext, K):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"  # Padding
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = (letter_to_number(plaintext[i]), letter_to_number(plaintext[i + 1]))
        result = (np.array(a) @ K) % 26
        ciphertext += number_to_letter(int(result[0])) + number_to_letter(int(result[1]))
    return ciphertext

def uncipher(ciphertext, K):
    k_inv = mod_inverse(K, 26)
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = (letter_to_number(ciphertext[i]), letter_to_number(ciphertext[i + 1]))
        result = (np.array(a) @ k_inv) % 26
        plaintext += number_to_letter(int(result[0])) + number_to_letter(int(result[1]))
    return plaintext

    


def main():
    while True:
        option = input("Ingrese 0 para encriptar o 1 para desencriptar: ")
        if option == "0":
            plaintext = input("Ingrese el texto a encriptar: ")
            K = input("Ingrese la clave K[0][0] K[0][1] K[1][0] K[1][1]: ")
            K = np.array(list(map(int, K.split()))).reshape(2, 2)
            ciphertext = cipher(plaintext, K)
            print("Texto encriptado:\n" + ciphertext + "\n")
        elif option == "1":
            ciphertext = input("Ingrese el texto a desencriptar: ")
            K = input("Ingrese la clave K[0][0] K[0][1] K[1][0] K[1][1]: ")
            K = np.array(list(map(int, K.split()))).reshape(2, 2)
            plaintext = uncipher(ciphertext, K)
            print("Texto desencriptado:\n" + plaintext + "\n")
        else:
            print("Opción inválida. Por favor ingrese 0 o 1.")


main()

# 11 8 3 7
# VKFZRVWTIAZSMISGKA
# JULY