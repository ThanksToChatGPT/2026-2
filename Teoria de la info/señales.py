import numpy as np
import matplotlib.pyplot as plt
import os

output_dir = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(output_dir, exist_ok=True)

def setup_transparent_dark_plot():
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=220)
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    # Ocultar espinas predeterminadas
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Dibujar ejes cartesianos limpios
    ax.axhline(0, color='white', linewidth=1.2, zorder=2)
    ax.axvline(0, color='white', linewidth=1.2, zorder=2)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.grid(True, linestyle='--', alpha=0.18, color='white')
    return fig, ax

def save_plot(fig, filename):
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, transparent=True, bbox_inches='tight')
    plt.close(fig)

# ==========================================
# 1. Escalón Unitario u(t)
# ==========================================
def plot_escalon():
    fig, ax = setup_transparent_dark_plot()
    t_neg = np.linspace(-3, 0, 300)
    t_pos = np.linspace(0, 3, 300)

    ax.plot(t_neg, np.zeros_like(t_neg), color='white', linewidth=2.5, zorder=3)
    ax.plot(t_pos, np.ones_like(t_pos), color='white', linewidth=2.5, zorder=3)
    ax.plot([0, 0], [0, 1], color='white', linestyle=':', linewidth=1.5, alpha=0.6)

    # Puntos clave
    ax.scatter([0], [0], facecolors='none', edgecolors='white', s=50, linewidth=2, zorder=5)
    ax.scatter([0], [1], facecolors='white', edgecolors='white', s=50, zorder=5)

    # Etiquetas de puntos
    ax.text(0.15, 1.05, r'$(0, 1)$', color='white', fontsize=10, weight='bold')
    ax.text(0.15, -0.15, r'$(0, 0)$', color='white', fontsize=10)
    ax.text(2.8, -0.2, r'$t$', color='white', fontsize=11, style='italic')
    ax.text(-0.35, 1.25, r'$u(t)$', color='white', fontsize=11, style='italic')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.4, 1.4)
    save_plot(fig, "escalon.png")

# ==========================================
# 2. Pulso Rectangular rect(t/T)
# ==========================================
def plot_rectangular():
    fig, ax = setup_transparent_dark_plot()
    half_T = 1.2

    t1 = np.linspace(-3, -half_T, 200)
    t2 = np.linspace(-half_T, half_T, 200)
    t3 = np.linspace(half_T, 3, 200)

    ax.plot(t1, np.zeros_like(t1), color='white', linewidth=2.5, zorder=3)
    ax.plot(t2, np.ones_like(t2), color='white', linewidth=2.5, zorder=3)
    ax.plot(t3, np.zeros_like(t3), color='white', linewidth=2.5, zorder=3)

    ax.plot([-half_T, -half_T], [0, 1], color='white', linestyle=':', linewidth=1.5, alpha=0.6)
    ax.plot([half_T, half_T], [0, 1], color='white', linestyle=':', linewidth=1.5, alpha=0.6)

    # Puntos clave
    ax.scatter([-half_T, half_T], [1, 1], facecolors='white', edgecolors='white', s=50, zorder=5)
    ax.scatter([-half_T, half_T], [0, 0], facecolors='none', edgecolors='white', s=50, linewidth=2, zorder=5)

    ax.text(-half_T - 0.45, -0.2, r'$-T/2$', color='white', fontsize=10, weight='bold')
    ax.text(half_T - 0.15, -0.2, r'$T/2$', color='white', fontsize=10, weight='bold')
    ax.text(-0.25, 1.05, r'$1$', color='white', fontsize=10, weight='bold')
    ax.text(0, 1.12, r'Ancho $= T$', color='white', fontsize=9, horizontalalignment='center')
    ax.text(2.8, -0.2, r'$t$', color='white', fontsize=11, style='italic')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.4, 1.4)
    save_plot(fig, "rectangular.png")

# ==========================================
# 3. Pulso Triangular tri(t/T)
# ==========================================
def plot_triangular():
    fig, ax = setup_transparent_dark_plot()
    T = 2.0

    t1 = np.linspace(-3.5, -T, 100)
    t2 = np.linspace(-T, 0, 200)
    t3 = np.linspace(0, T, 200)
    t4 = np.linspace(T, 3.5, 100)

    y2 = t2 / T + 1.0
    y3 = -t3 / T + 1.0

    ax.plot(t1, np.zeros_like(t1), color='white', linewidth=2.5, zorder=3)
    ax.plot(t2, y2, color='white', linewidth=2.5, zorder=3)
    ax.plot(t3, y3, color='white', linewidth=2.5, zorder=3)
    ax.plot(t4, np.zeros_like(t4), color='white', linewidth=2.5, zorder=3)

    # Puntos clave
    ax.scatter([-T, 0, T], [0, 1, 0], facecolors='white', edgecolors='white', s=50, zorder=5)
    ax.text(-T - 0.35, -0.2, r'$-T$', color='white', fontsize=10, weight='bold')
    ax.text(T - 0.1, -0.2, r'$T$', color='white', fontsize=10, weight='bold')
    ax.text(0.12, 1.05, r'$(0, 1)$', color='white', fontsize=10, weight='bold')
    ax.text(3.3, -0.2, r'$t$', color='white', fontsize=11, style='italic')

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.35, 1.35)
    save_plot(fig, "triangular.png")

# ==========================================
# 4. Función Rampa r(t)
# ==========================================
def plot_rampa():
    fig, ax = setup_transparent_dark_plot()
    t_neg = np.linspace(-3, 0, 200)
    t_pos = np.linspace(0, 3, 200)

    ax.plot(t_neg, np.zeros_like(t_neg), color='white', linewidth=2.5, zorder=3)
    ax.plot(t_pos, t_pos, color='white', linewidth=2.5, zorder=3)

    # Puntos clave
    ax.scatter([0, 1, 2], [0, 1, 2], facecolors='white', edgecolors='white', s=50, zorder=5)
    ax.plot([1, 1, 0], [0, 1, 1], color='white', linestyle=':', linewidth=1.2, alpha=0.6)
    ax.plot([2, 2, 0], [0, 2, 2], color='white', linestyle=':', linewidth=1.2, alpha=0.6)

    ax.text(0.15, -0.25, r'$(0, 0)$', color='white', fontsize=10)
    ax.text(1.15, 0.95, r'$(1, 1)$', color='white', fontsize=10, weight='bold')
    ax.text(2.15, 1.95, r'$(2, 2)$', color='white', fontsize=10, weight='bold')
    ax.text(1.2, 2.3, r'Pendiente $m=1$', color='white', fontsize=9.5, style='italic')
    ax.text(2.8, -0.25, r'$t$', color='white', fontsize=11, style='italic')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.5, 3.2)
    save_plot(fig, "rampa.png")

# ==========================================
# 5. Función Sinc(t)
# ==========================================
def plot_sinc():
    fig, ax = setup_transparent_dark_plot()
    t = np.linspace(-3.8, 3.8, 1000)
    y = np.sinc(t)

    ax.plot(t, y, color='white', linewidth=2.5, zorder=3)

    # Cruces por cero y máximo
    ceros = np.array([-3, -2, -1, 1, 2, 3])
    ax.scatter(ceros, np.zeros_like(ceros), facecolors='white', edgecolors='white', s=40, zorder=5)
    ax.scatter([0], [1], facecolors='white', edgecolors='white', s=50, zorder=5)

    ax.text(0.15, 1.05, r'Máximo $(0, 1)$', color='white', fontsize=10, weight='bold')
    for z in ceros:
        ax.text(z - 0.08, -0.16, str(z), color='white', fontsize=9, weight='bold')

    ax.text(3.6, -0.16, r'$t$', color='white', fontsize=11, style='italic')

    ax.set_xlim(-3.8, 3.8)
    ax.set_ylim(-0.35, 1.3)
    save_plot(fig, "sinc.png")

# ==========================================
# 6. Delta de Dirac delta(t)
# ==========================================
def plot_dirac():
    fig, ax = setup_transparent_dark_plot()
    t = np.linspace(-3, 3, 300)

    # Línea base en 0
    ax.plot(t, np.zeros_like(t), color='white', linewidth=2.5, zorder=3)

    # Flecha representando el impulso unitario
    ax.annotate('', xy=(0, 1.2), xytext=(0, 0),
                arrowprops=dict(facecolor='white', edgecolor='white', width=2.5, headwidth=10, headlength=12),
                zorder=5)

    # Punto en el origen y texto de área/peso
    ax.scatter([0], [0], facecolors='white', edgecolors='white', s=45, zorder=5)
    ax.text(0.15, 1.15, r'Área $= 1$', color='white', fontsize=11, weight='bold')
    ax.text(0.15, -0.18, r'$t = 0$', color='white', fontsize=10)
    ax.text(2.8, -0.18, r'$t$', color='white', fontsize=11, style='italic')
    ax.text(-0.55, 1.25, r'$\delta(t)$', color='white', fontsize=12, style='italic')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.35, 1.45)
    save_plot(fig, "dirac.png")

# ==========================================
# 7. Exponencial Compleja x(t) = A e^{j(\omega_0 t + \theta)}
# ==========================================
def plot_exponencial_compleja():
    fig, ax = setup_transparent_dark_plot()
    t = np.linspace(-3, 3, 600)
    # Ejemplo: A = 1, omega_0 = pi, theta = 0 -> Re = cos(pi*t), Im = sin(pi*t)
    re = np.cos(np.pi * t)
    im = np.sin(np.pi * t)

    ax.plot(t, re, color='white', linewidth=2.5, label=r'$\mathrm{Re}\{x(t)\} = A\cos(\omega_0 t + \theta)$', zorder=4)
    ax.plot(t, im, color='white', linewidth=1.8, linestyle='--', alpha=0.7, label=r'$\mathrm{Im}\{x(t)\} = A\sin(\omega_0 t + \theta)$', zorder=3)

    # Puntos clave en crestas/cruces
    ax.scatter([0, 1, 2], [1, -1, 1], facecolors='white', edgecolors='white', s=45, zorder=5)
    ax.text(0.12, 1.08, r'$+A$', color='white', fontsize=10, weight='bold')
    ax.text(1.12, -1.15, r'$-A$', color='white', fontsize=10, weight='bold')
    ax.text(2.8, -0.2, r'$t$', color='white', fontsize=11, style='italic')

    # Leyenda estilizada sin marco
    legend = ax.legend(loc='upper right', frameon=False, fontsize=9.5)
    for text in legend.get_texts():
        text.set_color('white')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.4, 1.4)
    save_plot(fig, "exponencial_compleja.png")

if __name__ == "__main__":
    plot_escalon()
    plot_rectangular()
    plot_triangular()
    plot_rampa()
    plot_sinc()
    plot_dirac()
    plot_exponencial_compleja()
    print("Todas las gráficas fueron generadas con éxito.")

