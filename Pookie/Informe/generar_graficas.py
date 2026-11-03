"""
================================================================================
LABORATORIO DE CONFORMADO MECÁNICO: LAMINACIÓN EN FRÍO
Script de Generación de Gráficas Analíticas en Calidad de Publicación (IEEE)
================================================================================

Este script genera las 5 gráficas cuantitativas de deformación plástica
para los tres materiales ensayados:
  1. Aleación de Aluminio (Pases 0 al 6)
  2. Aleación de Cobre (Pases 0 al 4)
  3. Acero Inoxidable (Pases 0 al 5)

Figuras generadas (300 DPI, formato PNG):
  - grafica_cw.png: Trabajo en frío (%CW) vs. Número de pases.
  - grafica_elongacion.png: Elongación longitudinal (%El) vs. Número de pases.
  - grafica_rh.png: Reducción porcentual de espesor (%Rh) vs. Número de pases.
  - grafica_deformacion.png: Deformación verdadera (epsilon) vs. Número de pases.

Estilo: Formato IEEE Transactions (serif/Times New Roman, STIX math,
grilla sutil, marcadores y estilos de línea accesibles para impresión en escala
de grises y alta visibilidad a color).
================================================================================
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# ==============================================================================
# 1. CONFIGURACIÓN GLOBAL Y ESTILO IEEE
# ==============================================================================

# Directorio de salida (por defecto el directorio donde reside este script)
OUTPUT_DIR = Path(__file__).resolve().parent

# Parámetros de publicación
DPI = 300
FIG_SIZE = (5.8, 4.0)  # Dimensiones optimizadas para columnas IEEE (~3.5" a 5.8")

# Paleta de colores representativos de cada aleación (Hexadecimal IEEE)
COLORES = {
    'Aluminio': {
        'linea': '#1565C0',        # Azul corporativo / metálico
        'relleno': '#42A5F5',      # Azul claro para relleno de marcador
        'borde': '#0D47A1',        # Azul marino oscuro para contorno
        'marcador': 'o',           # Círculo
        'estilo_linea': '-',       # Línea continua
        'nombre_leyenda': 'Aleación de Aluminio'
    },
    'Cobre': {
        'linea': '#C0392B',        # Terracota / Cobre rojizo
        'relleno': '#E67E22',      # Naranja cobrizo
        'borde': '#78281F',        # Caoba intenso
        'marcador': 's',           # Cuadrado
        'estilo_linea': '--',      # Línea discontinua
        'nombre_leyenda': 'Aleación de Cobre'
    },
    'AceroInox': {
        'linea': '#2C3E50',        # Gris acero / antracita
        'relleno': '#78909C',      # Gris azulado / acero pulido
        'borde': '#1A252F',        # Negro carbón
        'marcador': '^',           # Triángulo hacia arriba
        'estilo_linea': '-.',      # Línea raya-punto
        'nombre_leyenda': 'Acero Inoxidable'
    }
}

# Configuración tipográfica y de ejes (Estilo IEEE Transactions)
def aplicar_estilo_ieee():
    """Configura rcParams de matplotlib para emular la tipografía IEEE."""
    plt.style.use('default')
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['Times New Roman', 'DejaVu Serif', 'Liberation Serif', 'serif'],
        'mathtext.fontset': 'stix',
        'font.size': 10.5,
        'axes.labelsize': 11,
        'axes.titlesize': 11.5,
        'xtick.labelsize': 9.5,
        'ytick.labelsize': 9.5,
        'legend.fontsize': 9.0,
        'figure.titlesize': 12,
        'axes.linewidth': 1.0,
        'axes.edgecolor': '#2B2B2B',
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.major.size': 4.0,
        'ytick.major.size': 4.0,
        'xtick.minor.size': 2.5,
        'ytick.minor.size': 2.5,
        'grid.alpha': 0.35,
        'grid.linestyle': '--',
        'grid.linewidth': 0.6,
        'grid.color': '#B0BEC5',
        'savefig.dpi': DPI,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05
    })

# ==============================================================================
# 2. BASE DE DATOS EXPERIMENTALES
# ==============================================================================

DATOS_EXPERIMENTALES = {
    'Aluminio': {
        'pases': [0, 1, 2, 3, 4, 5, 6],
        'cw': [0.0, 0.0, 26.12, 45.02, 59.83, 76.37, 92.79],
        'el': [0.0, 4.24, 6.51, 25.45, 58.30, 146.12, 1279.93],
        'rh': [0.0, 34.38, 48.44, 59.38, 68.75, 84.38, 96.88],
        'eps': [0.0, 0.421, 0.662, 0.901, 1.163, 1.856, 3.466],
        'db': [0.0, 20.31, 12.50, 6.25, 0.94, 18.75, 81.25]
    },
    'Cobre': {
        'pases': [0, 1, 2, 3, 4],
        'cw': [0.0, 0.0, 0.0, 44.70, 63.82],
        'el': [0.0, 0.77, 10.53, 58.43, 173.26],
        'rh': [0.0, 19.15, 40.43, 74.47, 86.21],
        'eps': [0.0, 0.213, 0.518, 1.365, 1.981],
        'db': [0.0, 18.72, 36.17, 70.21, 106.38]
    },
    'AceroInox': {
        'pases': [0, 1, 2, 3, 4, 5],
        'cw': [0.0, 0.0, 9.23, 28.05, 59.02, 71.43],
        'el': [0.0, 14.74, 34.21, 62.63, 197.37, 326.32],
        'rh': [0.0, 13.56, 38.92, 61.84, 83.99, 88.88],
        'eps': [0.0, 0.146, 0.493, 0.963, 1.832, 2.196],
        'db': [0.0, 5.14, 16.72, 48.06, 101.05, 101.81]
    }
}

# ==============================================================================
# 3. FUNCIONES DE APOYO PARA GRAFICACIÓN
# ==============================================================================

def trazar_serie(ax, clave_material, x_vals, y_vals, ms=6.5, lw=2.0, alpha=0.95):
    """Traza una curva con marcadores y estilo distintivo según el material."""
    cfg = COLORES[clave_material]
    return ax.plot(
        x_vals,
        y_vals,
        marker=cfg['marcador'],
        color=cfg['linea'],
        linestyle=cfg['estilo_linea'],
        linewidth=lw,
        markersize=ms,
        markerfacecolor=cfg['relleno'],
        markeredgecolor=cfg['borde'],
        markeredgewidth=1.2,
        label=cfg['nombre_leyenda'],
        alpha=alpha,
        zorder=4
    )

def agregar_leyenda(ax, loc='best'):
    """Agrega la leyenda con formato estandarizado IEEE."""
    return ax.legend(
        loc=loc,
        frameon=True,
        facecolor='white',
        edgecolor='#BDBDBD',
        framealpha=0.92,
        fancybox=False,
        shadow=False
    )

# ==============================================================================
# 4. GENERADORES INDIVIDUALES DE LAS 5 GRÁFICAS
# ==============================================================================

def generar_grafica_cw(output_path):
    """
    Gráfica 1: Porcentaje de Trabajo en Frío (%CW) vs. Número de pases.
    %CW = (A0 - Af) / A0 * 100%
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for mat in ['Aluminio', 'Cobre', 'AceroInox']:
        trazar_serie(ax, mat, DATOS_EXPERIMENTALES[mat]['pases'], DATOS_EXPERIMENTALES[mat]['cw'])

    ax.set_title(r'Porcentaje de Trabajo en Frío ($\%CW$) vs. Número de Pases', fontweight='bold', pad=10)
    ax.set_xlabel(r'Número de Pases')
    ax.set_ylabel(r'Trabajo en Frío Acumulado, $\%CW$ (%)')

    ax.set_xlim(-0.25, 6.25)
    ax.set_ylim(-3, 103)
    ax.set_xticks(range(7))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

    ax.grid(True, which='major', linestyle='--', alpha=0.45)
    ax.grid(True, which='minor', linestyle=':', alpha=0.25)
    agregar_leyenda(ax, loc='upper left')

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI)
    plt.close(fig)
    print(f"[OK] Guardada: {output_path.name}")


def generar_grafica_elongacion(output_path):
    """
    Gráfica 2: Porcentaje de Elongación Longitudinal (%El) vs. Número de pases.
    %El = (Lf - L0) / L0 * 100%
    Debido a que el aluminio alcanza 1279.93% en el pase 6 mientras los primeros
    pases se ubican entre 0% y 10%, se utiliza una escala semilogarítmica simétrica
    (symlog con umbral lineal <= 1%) que preserva el valor 0 en el pase 0 y permite
    visualizar con perfecta resolución los 4 órdenes de magnitud del ensayo.
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for mat in ['Aluminio', 'Cobre', 'AceroInox']:
        trazar_serie(ax, mat, DATOS_EXPERIMENTALES[mat]['pases'], DATOS_EXPERIMENTALES[mat]['el'])

    ax.set_title(r'Elongación Longitudinal ($\%El$) vs. Número de Pases', fontweight='bold', pad=10)
    ax.set_xlabel(r'Número de Pases')
    ax.set_ylabel(r'Elongación Longitudinal, $\%El$ (%) [Escala Logarítmica]')

    # Escala symlog para abarcar desde 0% hasta 1280%
    ax.set_yscale('symlog', linthresh=1.0, linscale=0.75)
    ax.set_xlim(-0.25, 6.25)
    ax.set_ylim(-0.15, 2500)
    ax.set_xticks(range(7))

    # Ticks en potencias de 10 con formato legible
    major_ticks = [0, 1, 10, 100, 1000]
    ax.set_yticks(major_ticks)
    ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())

    ax.grid(True, which='major', linestyle='--', alpha=0.5)
    ax.grid(True, which='minor', linestyle=':', alpha=0.25)

    # Anotación técnica del punto extremo de aluminio en el pase 6
    al_x_final = DATOS_EXPERIMENTALES['Aluminio']['pases'][-1]
    al_y_final = DATOS_EXPERIMENTALES['Aluminio']['el'][-1]
    ax.annotate(
        f'{al_y_final:.1f}% (Pase 6)',
        xy=(al_x_final, al_y_final),
        xytext=(al_x_final - 1.6, al_y_final * 0.95),
        arrowprops=dict(arrowstyle='->', color='#0D47A1', lw=1.2),
        fontsize=8.5,
        fontweight='bold',
        color='#0D47A1',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor='#90CAF9', alpha=0.9)
    )

    # Anotación técnica del punto final de acero inoxidable
    ss_x_final = DATOS_EXPERIMENTALES['AceroInox']['pases'][-1]
    ss_y_final = DATOS_EXPERIMENTALES['AceroInox']['el'][-1]
    ax.annotate(
        f'{ss_y_final:.1f}%',
        xy=(ss_x_final, ss_y_final),
        xytext=(ss_x_final + 0.15, ss_y_final * 1.05),
        fontsize=8.0,
        fontweight='bold',
        color='#2C3E50'
    )

    # Anotación técnica del punto final de aleación de cobre
    cu_x_final = DATOS_EXPERIMENTALES['Cobre']['pases'][-1]
    cu_y_final = DATOS_EXPERIMENTALES['Cobre']['el'][-1]
    ax.annotate(
        f'{cu_y_final:.1f}%',
        xy=(cu_x_final, cu_y_final),
        xytext=(cu_x_final - 0.9, cu_y_final * 1.25),
        fontsize=8.0,
        fontweight='bold',
        color='#C0392B'
    )

    agregar_leyenda(ax, loc='upper left')

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI)
    plt.close(fig)
    print(f"[OK] Guardada: {output_path.name}")


def generar_grafica_rh(output_path):
    """
    Gráfica 3: Reducción porcentual de espesor (%Rh) vs. Número de pases.
    %Rh = (h0 - hf) / h0 * 100%
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for mat in ['Aluminio', 'Cobre', 'AceroInox']:
        trazar_serie(ax, mat, DATOS_EXPERIMENTALES[mat]['pases'], DATOS_EXPERIMENTALES[mat]['rh'])

    ax.set_title(r'Reducción de Espesor ($\%Rh$) vs. Número de Pases', fontweight='bold', pad=10)
    ax.set_xlabel(r'Número de Pases')
    ax.set_ylabel(r'Reducción Porcentual de Espesor, $\%Rh$ (%)')

    ax.set_xlim(-0.25, 6.25)
    ax.set_ylim(-3, 105)
    ax.set_xticks(range(7))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

    ax.grid(True, which='major', linestyle='--', alpha=0.45)
    ax.grid(True, which='minor', linestyle=':', alpha=0.25)
    agregar_leyenda(ax, loc='lower right')

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI)
    plt.close(fig)
    print(f"[OK] Guardada: {output_path.name}")


def generar_grafica_deformacion(output_path):
    """
    Gráfica 4: Deformación Verdadera (epsilon) vs. Número de pases.
    epsilon = ln(h0 / hf)
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for mat in ['Aluminio', 'Cobre', 'AceroInox']:
        trazar_serie(ax, mat, DATOS_EXPERIMENTALES[mat]['pases'], DATOS_EXPERIMENTALES[mat]['eps'])

    ax.set_title(r'Deformación Verdadera ($\varepsilon = \ln(h_0/h)$) vs. Número de Pases', fontweight='bold', pad=10)
    ax.set_xlabel(r'Número de Pases')
    ax.set_ylabel(r'Deformación Verdadera Acumulada, $\varepsilon$')

    ax.set_xlim(-0.25, 6.25)
    ax.set_ylim(-0.1, 3.8)
    ax.set_xticks(range(7))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

    ax.grid(True, which='major', linestyle='--', alpha=0.45)
    ax.grid(True, which='minor', linestyle=':', alpha=0.25)

    # Anotación del valor máximo alcanzado por el aluminio (epsilon = 3.466)
    ax.annotate(
        r'$\varepsilon_{max} = 3.466$',
        xy=(6, 3.466),
        xytext=(4.3, 3.35),
        arrowprops=dict(arrowstyle='->', color='#0D47A1', lw=1.2),
        fontsize=8.5,
        fontweight='bold',
        color='#0D47A1',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor='#90CAF9', alpha=0.9)
    )

    agregar_leyenda(ax, loc='upper left')

    fig.tight_layout()
    fig.savefig(output_path, dpi=DPI)
    plt.close(fig)
    print(f"[OK] Guardada: {output_path.name}")


def generar_grafica_ensanchamiento(output_path, incluir_inset=True):
    """
    Gráfica 5: Ensanchamiento Lateral (%Δb) vs. Porcentaje de Elongación (%El).
    %Δb = (b - b0) / b0 * 100%
    Muestra la correlación bidimensional del flujo plástico. Debido a que el
    aluminio alcanza una elongación de 1279.93% con ensanchamiento de 81.25%,
    mientras el cobre y el acero alcanzan ensanchamientos superiores al 100%
    con elongaciones menores a 400%, se incluye un recuadro de acercamiento
    (inset zoom) de alta resolución en la región 0% <= %El <= 200% para apreciar
    la marcada diferencia de pendientes y la severa anisotropía de flujo.
    """
    fig, ax = plt.subplots(figsize=FIG_SIZE)

    for mat in ['Aluminio', 'Cobre', 'AceroInox']:
        trazar_serie(ax, mat, DATOS_EXPERIMENTALES[mat]['el'], DATOS_EXPERIMENTALES[mat]['db'])

    ax.set_title(r'Ensanchamiento Lateral ($\%\Delta b$) vs. Elongación ($\%El$)', fontweight='bold', pad=10)
    ax.set_xlabel(r'Porcentaje de Elongación Longitudinal, $\%El$ (\%)')
    ax.set_ylabel(r'Ensanchamiento Lateral, $\%\Delta b$ (%)')

    ax.set_xlim(-25, 1350)
    ax.set_ylim(-5, 125)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(200))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(100))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))

    ax.grid(True, which='major', linestyle='--', alpha=0.45)
    ax.grid(True, which='minor', linestyle=':', alpha=0.25)

    # Leyenda ubicada en zona inferior derecha despejada
    agregar_leyenda(ax, loc='lower right')
    fig.tight_layout()

    # Inset axes para ampliar la zona de bajas y moderadas elongaciones (%El <= 200%)
    if incluir_inset:
        axins = inset_axes(
            ax,
            width="42%",
            height="42%",
            loc='upper right',
            bbox_to_anchor=(-0.08, -0.04, 0.98, 0.98),
            bbox_transform=ax.transAxes,
            borderpad=0.5
        )
        for mat in ['Aluminio', 'Cobre', 'AceroInox']:
            trazar_serie(axins, mat, DATOS_EXPERIMENTALES[mat]['el'], DATOS_EXPERIMENTALES[mat]['db'], ms=4.2, lw=1.5)

        axins.set_xlim(-5, 200)
        axins.set_ylim(-5, 115)
        axins.set_title(r'Detalle: $\%El \leq 200\%$', fontsize=8.0, fontweight='bold', pad=3)
        axins.tick_params(axis='both', which='major', labelsize=7.5)
        axins.xaxis.set_major_locator(ticker.MultipleLocator(50))
        axins.yaxis.set_major_locator(ticker.MultipleLocator(25))
        axins.grid(True, which='major', linestyle='--', alpha=0.4)
        axins.set_facecolor('#FAFAFA')

        # Conectores y caja indicadora
        mark_inset(ax, axins, loc1=2, loc2=4, fc='none', ec='#757575', ls=':', lw=0.9)

    # Anotación técnica del punto final de aluminio
    ax.annotate(
        r'Al: $\%El=1280\%$, $\%\Delta b=81.3\%$',
        xy=(1279.93, 81.25),
        xytext=(920, 68),
        arrowprops=dict(arrowstyle='->', color='#0D47A1', lw=1.1),
        fontsize=8.0,
        fontweight='bold',
        color='#0D47A1',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD', edgecolor='#90CAF9', alpha=0.92)
    )

    fig.savefig(output_path, dpi=DPI, bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Guardada: {output_path.name}")


# ==============================================================================
# 5. EJECUCIÓN PRINCIPAL
# ==============================================================================

def main():
    """Genera las 5 gráficas del laboratorio en alta resolución (300 DPI)."""
    aplicar_estilo_ieee()

    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("GENERADOR DE GRÁFICAS DE LAMINACIÓN EN FRÍO (ESTILO IEEE)")
    print(f"Directorio de destino: {output_dir}")
    print(f"Resolución de salida : {DPI} DPI")
    print("=" * 60)

    archivos = {
        'grafica_cw.png': generar_grafica_cw,
        'grafica_elongacion.png': generar_grafica_elongacion,
        'grafica_rh.png': generar_grafica_rh,
        'grafica_deformacion.png': generar_grafica_deformacion,
    }

    for nombre_archivo, funcion_graficadora in archivos.items():
        ruta_archivo = output_dir / nombre_archivo
        funcion_graficadora(ruta_archivo)

    print("=" * 60)
    print("¡Las 5 gráficas fueron generadas exitosamente!")
    print("=" * 60)


if __name__ == '__main__':
    main()
