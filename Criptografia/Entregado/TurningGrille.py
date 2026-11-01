# Turning Grille cipher (Rejilla de Fleissner)

def rotar_hoyos(hoyos, n, direccion):
    # Rota las coordenadas de los hoyos 90 grados
    # direccion = 1: sentido horario -> (r, c) -> (c, n - 1 - r)
    # direccion = 0: sentido antihorario -> (r, c) -> (n - 1 - c, r)
    if direccion == 1:
        return [(c, n - 1 - r) for r, c in hoyos]
    else:
        return [(n - 1 - c, r) for r, c in hoyos]


def parse_hoyos(texto):
    # Recibe los hoyos en el formato "a b;c d;e f;"
    hoyos = []
    for par in texto.split(";"):
        if par.strip():
            fila, col = par.split()
            hoyos.append((int(fila), int(col)))
    return hoyos


def encrypt(plaintext, n, direccion, hoyos):
    # Asegurarse de que el texto esté en mayúsculas y sin espacios
    plaintext = plaintext.upper().replace(" ", "")
    block_size = n * n

    # Rellenar con 'X' si no es múltiplo de n*n
    if len(plaintext) % block_size != 0:
        plaintext += 'X' * (block_size - (len(plaintext) % block_size))

    ciphertext = ""
    # Procesar bloque por bloque
    for b in range(0, len(plaintext), block_size):
        bloque = plaintext[b:b + block_size]
        grid = [['' for _ in range(n)] for _ in range(n)]
        visited = set()
        curr_hoyos = list(hoyos)
        idx = 0

        # 4 rotaciones de la rejilla
        for rot in range(4):
            for r, c in sorted(curr_hoyos):
                if (r, c) not in visited:
                    grid[r][c] = bloque[idx]
                    idx += 1
                    visited.add((r, c))
            curr_hoyos = rotar_hoyos(curr_hoyos, n, direccion)

        # Leer la matriz por filas
        for r in range(n):
            for c in range(n):
                ciphertext += grid[r][c]

    # Dividir el output en bloques del tamaño de la retícula
    return " ".join(ciphertext[i:i + n] for i in range(0, len(ciphertext), n))


def decrypt(ciphertext, n, direccion, hoyos):
    # Asegurarse de que el texto esté en mayúsculas y sin espacios
    ciphertext = ciphertext.upper().replace(" ", "")
    block_size = n * n

    if len(ciphertext) % block_size != 0:
        ciphertext += 'X' * (block_size - (len(ciphertext) % block_size))

    plaintext = ""
    # Procesar bloque por bloque
    for b in range(0, len(ciphertext), block_size):
        bloque = ciphertext[b:b + block_size]
        # Llenar la cuadrícula fila por fila con el texto cifrado
        grid = [[bloque[r * n + c] for c in range(n)] for r in range(n)]
        visited = set()
        curr_hoyos = list(hoyos)

        # 4 rotaciones de la rejilla
        for rot in range(4):
            for r, c in sorted(curr_hoyos):
                if (r, c) not in visited:
                    plaintext += grid[r][c]
                    visited.add((r, c))
            curr_hoyos = rotar_hoyos(curr_hoyos, n, direccion)

    return plaintext


def main():
    while True:
        try:
            n = int(input("Ingrese el tamaño de la retícula: "))
            direccion = int(input("Ingrese la dirección de rotación (1 horario, 0 antihorario): "))
            modo = int(input("Ingrese el modo (1 cifrar, 0 descifrar): "))
            hoyos_str = input("Ingrese los hoyos (ej: 0 0;2 1;2 3;3 2;): ")
            hoyos = parse_hoyos(hoyos_str)

            if modo == 1:
                plaintext = input("Ingrese el texto a encriptar: ")
                ciphertext = encrypt(plaintext, n, direccion, hoyos)
                print("Texto encriptado:\n" + ciphertext + "\n")
            elif modo == 0:
                ciphertext = input("Ingrese el texto a desencriptar: ")
                plaintext = decrypt(ciphertext, n, direccion, hoyos)
                print("Texto desencriptado:\n" + plaintext + "\n")
            else:
                print("Opción inválida. Por favor ingrese 1 o 0.\n")

        except (EOFError, KeyboardInterrupt):
            break
        except Exception as e:
            print(f"Error: {e}\n")

main()


# JIM ATTACKS AT DAWN
# 0 0;2 1;2 3;3 2;
# JKTD SAAT WIAM CNAT

# TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I
# 0 0;0 3;0 5;1 2;1 8;2 1;2 6;3 2;3 4;3 7;4 4;4 6;4 8;5 3;5 7;6 0;6 5;7 1;7 4;7 8;8 2;
# THIS IS A MESSAGE THAT I AM ENCRYPTING WITH A TURNING GRILLE TO PROVIDE THIS ILLUSTRATIVE EXAMPLE