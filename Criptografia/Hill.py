import numpy as np
def letter_to_number(letter):
    return ord(letter) - 65

def number_to_letter(number):
    return chr(number + 65)

def cipher(plaintext, k, t):
    plaintext = plaintext.upper().replace(" ", "")
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a = 
        


def uncipher(ciphertext, k_inv):
    ciphertext = ciphertext.upper().replace(" ", "")
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a = (letter_to_number(ciphertext[i]), letter_to_number(ciphertext[i + 1]))
        result = np.array(a) @ k_inv
        result = result % 26
        plaintext += number_to_letter(int(result[0])) + number_to_letter(int(result[1]))
    return plaintext
    


k = [[7, 18], [23, 11]]
cipher = "VKFZRVWTIAZSMISGKA"

unciphered_text = uncipher(cipher, k)
print("Texto desencriptado:\n" + unciphered_text + "\n")