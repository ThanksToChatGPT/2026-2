import sys
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. MÓDULO MATEMÁTICO Y DE VISUALIZACIÓN
# ==========================================

def configurar_grafico(titulo):
    """Configura el lienzo de matplotlib para el plano complejo."""
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title(titulo)
    plt.xlabel('Eje Real (Re)')
    plt.ylabel('Eje Imaginario (Im)')

def graficar_vector(z, color, etiqueta, flecha=True):
    """Dibuja un punto y opcionalmente su vector desde el origen."""
    plt.plot(z.real, z.imag, marker='o', color=color, label=etiqueta)
    if flecha:
        plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color=color, alpha=0.6)

def mostrar_grafico():
    plt.legend()
    plt.axis('equal')
    plt.show()

# ==========================================
# 2. MÓDULO DE OPERACIONES COMPLEJAS
# ==========================================

def graficar_exponenciacion(z):
    print("\n--- Calculando Exponenciación ---")
    configurar_grafico(f"Exponenciación: $e^{{{z.real} + {z.imag}i}}$")
    ez = np.exp(z)
    graficar_vector(z, 'blue', f'z = {z:.2f}')
    graficar_vector(ez, 'red', f'$e^z$ = {ez:.2f}')
    mostrar_grafico()

def graficar_logaritmo(z):
    print("\n--- Calculando Logaritmo Principal ---")
    if z == 0:
        print("[!] Error: El logaritmo de 0 no está definido.")
        return
    configurar_grafico(f"Logaritmo Principal: $Ln(z)$")
    lnz = np.log(z) 
    graficar_vector(z, 'blue', f'z = {z:.2f}')
    graficar_vector(lnz, 'green', f'Ln(z) = {lnz:.2f}')
    mostrar_grafico()

def graficar_potenciacion(z, n):
    print(f"\n--- Calculando Potenciación (z^{n}) ---")
    configurar_grafico(f"Potenciación: $z^{{{n}}}$")
    zn = z ** n
    graficar_vector(z, 'blue', f'z = {z:.2f}')
    graficar_vector(zn, 'purple', f'$z^{{{n}}}$ = {zn:.2f}')
    mostrar_grafico()

def graficar_radicacion(z, n):
    print(f"\n--- Calculando Radicación (Raíces {n}-ésimas) ---")
    if n <= 0:
        print("[!] Error: El valor de 'n' debe ser un entero positivo mayor a 0.")
        return
    if z == 0:
        print("[!] Error: La radicación de 0 es trivial (0).")
        return
        
    configurar_grafico(f"Radicación: Raíces {n}-ésimas de z")
    graficar_vector(z, 'blue', f'z = {z:.2f}')
    
    r = np.abs(z)
    theta = np.angle(z)
    raices = []
    
    # Cálculo de raíces usando forma polar fraccionaria
    for k in range(n):
        raiz = (r**(1/n)) * np.exp(1j * (theta + 2*np.pi*k) / n)
        raices.append(raiz)
        graficar_vector(raiz, 'orange', f'$w_{k}$', flecha=False)
        
    # Dibujar polígono regular conectando las raíces
    raices.append(raices[0])
    raices_np = np.array(raices)
    plt.plot(raices_np.real, raices_np.imag, 'r--', alpha=0.5, label=f'Polígono de {n} lados')
    
    # Dibujar circunferencia donde descansan las raíces
    circulo = plt.Circle((0, 0), r**(1/n), color='orange', fill=False, linestyle='dotted', label=r'Circunferencia $R=\sqrt[n]{r}$')
    plt.gca().add_patch(circulo)
    
    mostrar_grafico()

# ==========================================
# 3. MÓDULO DE INTERFAZ DE TERMINAL (CLI)
# ==========================================

def solicitar_complejo():
    """Solicita al usuario las partes real e imaginaria con manejo de errores."""
    while True:
        try:
            print("\nIngrese el número complejo (z = x + iy):")
            x = float(input("Parte Real (x): "))
            y = float(input("Parte Imaginaria (y): "))
            return complex(x, y)
        except ValueError:
            print("[!] Entrada inválida. Por favor, ingrese valores numéricos (ej. 1, -2.5, 3).")

def solicitar_n(texto="Ingrese el valor de 'n' (entero positivo): "):
    """Solicita un número entero para potenciación o radicación."""
    while True:
        try:
            n = int(input(f"\n{texto}"))
            return n
        except ValueError:
            print("[!] Entrada inválida. Por favor, ingrese un número entero.")

def menu_principal():
    """Ejecuta el bucle del menú interactivo en la terminal."""
    while True:
        print("\n" + "="*40)
        print("  CALCULADORA GRÁFICA DE COMPLEJOS  ")
        print("="*40)
        print("1. Exponenciación (e^z)")
        print("2. Logaritmo Principal Ln(z)")
        print("3. Potenciación (z^n)")
        print("4. Radicación (Raíces n-ésimas de z)")
        print("5. Salir")
        print("="*40)
        
        opcion = input("Seleccione una operación (1-5): ")
        
        if opcion == '1':
            z = solicitar_complejo()
            graficar_exponenciacion(z)
        elif opcion == '2':
            z = solicitar_complejo()
            graficar_logaritmo(z)
        elif opcion == '3':
            z = solicitar_complejo()
            n = solicitar_n("Ingrese la potencia 'n' (entero): ")
            graficar_potenciacion(z, n)
        elif opcion == '4':
            z = solicitar_complejo()
            n = solicitar_n("Ingrese el grado de la raíz 'n' (entero > 0): ")
            graficar_radicacion(z, n)
        elif opcion == '5':
            print("\nSaliendo del programa... ¡Hasta luego!")
            sys.exit(0)
        else:
            print("\n[!] Opción no válida. Por favor seleccione un número del 1 al 5.")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario. Saliendo...")
        sys.exit(0)