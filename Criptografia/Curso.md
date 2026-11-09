# Criptografia

- Pagina: https://sites.google.com/view/crypto-2026-2
- Diapositivas: https://drive.google.com/drive/folders/1mosIUshNXGZx8aqj9hnr-jDt2JkVdOKr

## Evaluacion

- Talleres: 40%
- Primer parcial: 15% 
- Presentacion y articulo: 15%
- Segundo parcial: 15%
- Proyecto: 15%

## Apuntes del Curso

- [01. Introduccion a la Criptografia y Seguridad de la Informacion](./Apuntes/01_Introduccion_a_la_Criptografia.md): `criptografia`, `criptoanalisis`, `criptologia`, `triada cia`, `confidencialidad`, `integridad`, `autenticacion`, `disponibilidad`, `no repudio`, `spoofing`, `alice y bob`, `eve`, `maggie`, `mallory`, `peggy`, `victor`, `one-time pad`, `otp`, `cifrado de vernam`, `secreto perfecto`, `perfect secrecy`, `shannon`, `xor`, `adicion mod 2`, `seguridad incondicional`, `seguridad computacional`, `principio de kerckhoffs`, `security by obscurity`, `two-time pad attack`.
- [02. Cifrado de Porta (Polygraphic Monoalphabetic)](./Apuntes/02_Cifrado_Porta.md): `porta cipher`, `cifrado poligrafico`, `monoalfabetico`, `tableau 20x20`, `digramas`, `glifos`, `giovanni battista della porta`, `sustitucion poligrafica`, `padding`, `alfabeto latino 20 letras`.
- [03. Cifrado Playfair (Playfair Polygraphic Cipher)](./Apuntes/03_Cifrado_Playfair.md): `playfair cipher`, `cifrado poligrafico`, `matriz 5x5`, `digramas`, `regla del rectangulo`, `charles wheatstone`, `lyon playfair`, `sustitucion monoalfabetica poligrafica`, `yoan pinzon`, `criptoanalisis digramas`.
- [04. Cifrado Cesar (Caesar's Cipher)](./Apuntes/04_Cifrado_Cesar.md): `caesar cipher`, `cifrado cesar`, `unilateral`, `monoalfabetico`, `modulo 26`, `desplazamiento`, `analisis de frecuencias`, `kama sutra`, `fuerza bruta`, `chi-cuadrado`, `indice de coincidencia`, `rot13`, `bloques de longitud 5`.
- [05. Cifrado ROT13 (Rot13 Cipher)](./Apuntes/05_Cifrado_Rot13.md): `rot13`, `cifrado cesar k=13`, `involutivo`, `autoinverso`, `usenet`, `ofuscacion`, `monoalfabetico unilateral`, `automapeo`, `rot47`, `propiedad involutiva`, `analisis de frecuencia`.
- [06. Cifrado de Puntos (Dots Cipher)](./Apuntes/06_Cifrado_Dots.md): `dots cipher`, `cifrado de puntos`, `pigpen`, `unilateral`, `monoalfabetico`, `sustitucion geometrica`, `simbolos graficos`, `cuadricula 3x3`, `marcos geometricos`, `analisis de frecuencia`.
- [07. Cifrado Garbage-in-between (Rejilla de Richelieu)](./Apuntes/07_Cifrado_Garbage_in_Between.md): `garbage-in-between`, `cardinal richelieu`, `multilateral`, `polifonico`, `rejilla esteganografica`, `mascara binaria`, `caracteres de relleno`, `chaffing`, `inyeccion de ruido`, `covert story`.
- [08. Cifrado Vigenere (Vigenere Polyalphabetic Cipher)](./Apuntes/08_Cifrado_Vigenere.md): `vigenere cipher`, `polialfabetico`, `tabula recta`, `keyword`, `kasiski`, `enigma`, `aplanamiento de frecuencias`, `blaise de vigenere`, `indice de coincidencia`, `friedman`, `modulo 26`, `sustitucion polialfabetica`, `le chiffre indechiffrable`.
- [09. Cifrado de Hill e Inversa Modular de Matrices](./Apuntes/09_Cifrado_Hill.md): `hill cipher`, `algebra lineal mod 26`, `matriz clave`, `inversa modular`, `algoritmo euclides extendido`, `eea`, `adjunta`, `determinante`, `lester s hill`, `cifrado de bloques`, `polialfabetico`, `identidad de bezout`, `known plaintext attack`, `kpa`, `cofactores`, `regla de laplace`, `matrices modulares`, `invertibilidad`.
- [10. Cifrado Homofonico (Homophonic Substitution Cipher)](./Apuntes/10_Cifrado_Homofonico.md): `homophonic cipher`, `sustitucion homofonica`, `alfabeto expandido`, `frecuencia de letras`, `combinatoria de layouts`, `estirling`, `coeficiente multinomial`, `surjecciones`, `histograma uniforme`, `criptoanalisis digramas`, `particion de homofonos`.
- [11. Cifrado de Rejilla Giratoria (Turning Grille / Fleissner)](./Apuntes/11_Cifrado_Rejilla_Giratoria.md): `turning grille`, `rejilla giratoria`, `fleissner`, `cifrado por transposicion`, `permutacion`, `4 rotaciones`, `matriz nxn`, `orbitas de rotacion`, `rejilla impar`, `crib analysis`, `criptoanalisis de transposicion`.
- [12. Cifrado Lucifer y Cifrados de Producto](./Apuntes/12_Cifrado_Lucifer.md): `lucifer cipher`, `cifrado de producto`, `feistel`, `s-box`, `p-box`, `confusion`, `difusion`, `des predecessor`, `red spn`, `claude shannon`, `sustitucion-permutacion`, `efecto avalancha`, `no linealidad`, `demonstration cipher`, `ibm 1971`.
- [13. Cifrado Hayhanen (VIC Cipher)](./Apuntes/13_Cifrado_Hayhanen.md): `hayhanen cipher`, `vic cipher`, `straddling checkerboard`, `doble transposicion`, `disrupcion`, `reino hayhanen`, `kgb`, `snegopad`, `hollow nickel`, `cifrado de producto`, `fraccionamiento`, `ruta zigzag`.
- [14. Modos de Operacion de Cifrados por Bloque](./Apuntes/14_Modos_de_Operacion_Bloque.md): `modos de operacion`, `ecb`, `cbc`, `cfb`, `ofb`, `ctr`, `vector de inicializacion`, `iv`, `propagacion de error`, `tux ecb`, `stream cipher`, `padding`, `registro de desplazamiento`, `electronic codebook`, `cipher block chaining`, `cipher feedback`, `output feedback`, `counter mode`, `two-time pad`.
- [Cifrado DES (Data Encryption Standard)](./Apuntes/Cifrado_DES.md): `data encryption standard`, `des`, `cifrado por bloques`, `red de feistel`, `64 bits`, `clave de 56 bits`, `bits de paridad`, `key schedule`, `pc-1`, `pc-2`, `desplazamiento circular`, `ls`, `permutacion inicial`, `ip`, `ip inversa`, `fp`, `funcion f`, `expansion e`, `cajas s`, `s-box`, `permutacion p`, `confusion`, `difusion`, `eff deep crack`, `inversion de mitades`, `padding ceros`.
- [15. AES: Estructura Global y Representacion del Estado](./Apuntes/15_AES_Estructura_Global.md): `aes`, `rijndael`, `fips 197`, `cifrado por bloques`, `state array`, `matriz de estado 4x4`, `orden column-major`, `nb`, `nk`, `nr`, `rondas aes`, `aes-128`, `aes-192`, `aes-256`, `etapas de cifrado`, `etapas de descifrado`, `whitening`, `ronda inicial`, `ronda final`.
- [16. AES: Generador y Expansion de Claves (Key Expansion)](./Apuntes/16_AES_KeyExpansion.md): `key expansion`, `key generator`, `rotword`, `subword`, `rcon`, `constante de ronda`, `subclaves`, `w[i]`, `aes-128`, `gf(2^8)`, `s-box`, `recursividad de claves`, `whitening key`.
- [17. AES: Transformacion AddRoundKey (ARK)](./Apuntes/17_AES_AddRoundKey.md): `addroundkey`, `ark`, `xor`, `key whitening`, `subclave`, `involutivo`, `autoinverso`, `state array`, `dependencia de clave`, `suma en gf(2)`.
- [18. AES: Transformacion SubBytes e InvSubBytes (SB)](./Apuntes/18_AES_SubBytes.md): `subbytes`, `invsubbytes`, `s-box`, `invsbox`, `caja s`, `confusion`, `no linealidad`, `sustitucion de bytes`, `nibble`, `gf(2^8)`, `inversion multiplicativa`, `transformacion afin`.
- [19. AES: Transformacion ShiftRows e InvShiftRows (SR)](./Apuntes/19_AES_ShiftRows.md): `shiftrows`, `invshiftrows`, `sr`, `desplazamiento ciclico`, `difusion horizontal`, `permutacion de bytes`, `state array`, `rotacion a la izquierda`, `rotacion a la derecha`, `inter-column mixing`.
- [20. AES: Transformacion MixColumns e InvMixColumns (MC)](./Apuntes/20_AES_MixColumns.md): `mixcolumns`, `invmixcolumns`, `mc`, `galois field`, `gf(2^8)`, `e-table`, `l-table`, `multiplicacion modular`, `difusion vertical`, `matriz mds`, `polinomio irreducible`, `operacion lineal`.
