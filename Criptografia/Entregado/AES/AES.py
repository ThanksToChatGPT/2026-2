# AES Image Encryption (Cifrado AES de imágenes)
import os
import sys
import base64

# Importar pyaes directamente desde la carpeta local
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pyaes

# Claves predeterminadas para cada nivel de seguridad
CLAVES = {
    128: b"\xfa\x16&\x11[\x9dr\xcf\x0cx\xcb\x11K\x06\x12\x13",
    192: b'\xcc\x02m\xca\x92U=\x7f\xa4\xc4R\x93\xdb 5"\xc67\x88\xa8\x86\xa8z\xfe',
    256: b"\xadx\xb2\rh\xb9\x91\x13\x9b\x04F\x84\x88\x884\x16@4\xfe@p\xe6\xeb\xa1^*s\xfa\x9f\xd0\xbe\xde"
}

IV = b"\0" * 16


def bytes_a_bits(datos):
    # Convierte secuencia de bytes en arreglo de bits
    return [(byte >> i) & 1 for byte in datos for i in range(7, -1, -1)]


def bits_a_bytes(bits):
    # Convierte arreglo de bits a bytes
    byte_list = bytearray()
    for i in range(0, len(bits), 8):
        byte_val = 0
        for b in bits[i:i + 8]:
            byte_val = (byte_val << 1) | int(b)
        byte_list.append(byte_val)
    return bytes(byte_list)


def imagen_a_bits(ruta_imagen):
    # Lee la imagen en binario y retorna sus bits
    with open(ruta_imagen, "rb") as f:
        return bytes_a_bits(f.read())


def bits_a_imagen(bits, ruta_salida):
    # Escribe los bits como bytes para recrear la imagen
    with open(ruta_salida, "wb") as f:
        f.write(bits_a_bytes(bits))


def cifrar(bits, nivel):
    # Cifra los bits usando AES-CBC con relleno PKCS#7
    clave = CLAVES[nivel]
    datos_bytes = bits_a_bytes(bits)
    encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(clave, IV))
    cifrado_bytes = encrypter.feed(datos_bytes) + encrypter.feed()
    return bytes_a_bits(cifrado_bytes)


def descifrar(bits_cifrados, nivel):
    # Descifra los bits usando AES-CBC
    clave = CLAVES[nivel]
    cifrado_bytes = bits_a_bytes(bits_cifrados)
    decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(clave, IV))
    descifrado_bytes = decrypter.feed(cifrado_bytes) + decrypter.feed()
    return bytes_a_bits(descifrado_bytes)


def codificar_base64(bits):
    # Codifica los bits a Base64
    return base64.b64encode(bits_a_bytes(bits)).decode("utf-8")


def decodificar_base64(texto_base64):
    # Decodifica de Base64 a bits
    return bytes_a_bits(base64.b64decode(texto_base64))


def main():
    # Parámetro de nivel de seguridad (128, 192 o 256 bits)
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        nivel = int(sys.argv[1])
    else:
        nivel = int(input("Ingrese el nivel de seguridad (128, 192, 256): "))

    ruta_imagen = input("Ingrese el nombre de la imagen a cifrar: ").strip().strip('"').strip("'")
    if not os.path.exists(ruta_imagen):
        ruta_alt = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_imagen)
        if os.path.exists(ruta_alt):
            ruta_imagen = ruta_alt

    nombre, ext = os.path.splitext(ruta_imagen)
    ruta_salida = f"{nombre}_recuperada{ext}"

    print(f"\n[+] Archivo: {ruta_imagen}")
    print(f"[+] Nivel de seguridad: AES-{nivel} bits")

    print("[+] Convirtiendo imagen a bits...")
    bits = imagen_a_bits(ruta_imagen)

    print(f"[+] Cifrando imagen con AES ({nivel} bits)...")
    bits_cifrados = cifrar(bits, nivel)

    print("[+] Codificando a Base64...")
    texto_base64 = codificar_base64(bits_cifrados)

    print("\nTexto en Base 64:")
    print(texto_base64)
    print()

    print("[+] Decodificando de Base64 a representación en bits...")
    bits_para_descifrar = decodificar_base64(texto_base64)

    print(f"[+] Descifrando con AES ({nivel} bits)...")
    bits_originales = descifrar(bits_para_descifrar, nivel)

    print(f"[+] Recreando la imagen original en '{ruta_salida}'...")
    bits_a_imagen(bits_originales, ruta_salida)

    print("¡Proceso completado exitosamente!\n")


if __name__ == "__main__":
    main()
