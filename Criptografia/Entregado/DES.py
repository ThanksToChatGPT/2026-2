# DES Image Encryption (Cifrado DES de imágenes)
import os
import base64
from pyDes import des, CBC, PAD_PKCS5

KEY = "133457799BBCDFF1"


def bytes_a_bits(datos):
    # Convierte una secuencia de bytes en un arreglo (lista) de bits (0 y 1)
    if isinstance(datos, list):
        return datos
    return [(byte >> i) & 1 for byte in datos for i in range(7, -1, -1)]


def bits_a_bytes(bits):
    # Convierte un arreglo de bits (o string de bits) a bytes
    if isinstance(bits, (bytes, bytearray)):
        return bytes(bits)
    if isinstance(bits, str):
        bits = [int(b) for b in bits if b in "01"]

    byte_list = bytearray()
    for i in range(0, len(bits), 8):
        byte_val = 0
        for b in bits[i:i + 8]:
            byte_val = (byte_val << 1) | int(b)
        byte_list.append(byte_val)
    return bytes(byte_list)


def parsear_clave(clave):
    # Convierte la clave a 8 bytes requeridos por DES
    if isinstance(clave, bytes):
        return clave
    if isinstance(clave, str):
        try:
            if len(clave) == 16:
                return bytes.fromhex(clave)
        except ValueError:
            pass
        return clave.encode("utf-8")[:8]
    return clave


def imagen_a_bits(ruta_imagen):
    # Recibe la imagen, la lee en modo binario y retorna su representación en bits
    with open(ruta_imagen, "rb") as f:
        datos = f.read()
    return bytes_a_bits(datos)


def cifrar(bits, clave=KEY):
    # Cifra la representación en bits usando DES y retorna el arreglo de bits cifrados
    datos_bytes = bits_a_bytes(bits)
    clave_bytes = parsear_clave(clave)

    # Cifrado DES en modo CBC con relleno PAD_PKCS5 y vector de inicialización en ceros
    d = des(clave_bytes, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    cifrado_bytes = d.encrypt(datos_bytes)

    return bytes_a_bits(cifrado_bytes)


def codificar_base64(datos):
    # Codifica los datos cifrados (bits o bytes) a formato Base64
    datos_bytes = bits_a_bytes(datos)
    return base64.b64encode(datos_bytes).decode("utf-8")


def decodificar_base64(texto_base64):
    # Decodifica de Base64 a la representación en bits
    datos_bytes = base64.b64decode(texto_base64)
    return bytes_a_bits(datos_bytes)


def descifrar(bits_cifrados, clave=KEY):
    # Descifra los bits cifrados utilizando DES y retorna la representación en bits original
    cifrado_bytes = bits_a_bytes(bits_cifrados)
    clave_bytes = parsear_clave(clave)

    d = des(clave_bytes, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    descifrado_bytes = d.decrypt(cifrado_bytes)

    return bytes_a_bits(descifrado_bytes)


def bits_a_imagen(bits, ruta_salida="imagen_recuperada.png"):
    # Convierte el arreglo de bits a bytes y guarda la imagen
    datos_bytes = bits_a_bytes(bits)
    with open(ruta_salida, "wb") as f:
        f.write(datos_bytes)


def main():
    while True:
        try:
            ruta_imagen = input("Ingrese la ruta de la imagen a cifrar (o 'salir'): ").strip().strip('"').strip("'").strip("\ufeff")
            if not ruta_imagen or ruta_imagen.lower() == "salir":
                break

            if not os.path.exists(ruta_imagen):
                print(f"Error: El archivo '{ruta_imagen}' no existe.\n")
                continue

            print("\n[+] Convirtiendo imagen a bits...")
            bits = imagen_a_bits(ruta_imagen)

            print("[+] Cifrando imagen con DES...")
            bits_cifrados = cifrar(bits, KEY)

            print("[+] Codificando a Base64...")
            texto_base64 = codificar_base64(bits_cifrados)

            print("\nTexto en Base 64:")
            print(texto_base64)
            print()

            print("[+] Decodificando de Base64 a representación en bits...")
            bits_para_descifrar = decodificar_base64(texto_base64)

            print("[+] Descifrando con DES...")
            bits_originales = descifrar(bits_para_descifrar, KEY)

            nombre, ext = os.path.splitext(ruta_imagen)
            ruta_salida = f"{nombre}_recuperada{ext}"

            print(f"[+] Generando y guardando la imagen original en '{ruta_salida}'...")
            bits_a_imagen(bits_originales, ruta_salida)

            print("¡Proceso completado exitosamente!\n")

        except (EOFError, KeyboardInterrupt):
            break
        except Exception as e:
            print(f"Error: {e}\n")


main()

# Clave DES: 133457799BBCDFF1
# Entrada de prueba: image.png