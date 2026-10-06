# Notas

### 1. Definición de una señal senoidal
- **Forma canónica**:
  $$x(t) = A \sin(2\pi f_0 t + \phi) = A \sin(\omega_0 t + \phi)$$
  *(o equivalente en coseno: $x(t) = A \cos(2\pi f_0 t + \phi)$)*.
- **Parámetros**:
  - $A$: **Amplitud** (valor pico de oscilación).
  - $f_0$: **Frecuencia lineal / cíclica** en Hertz ($\text{Hz} = \text{s}^{-1}$), ciclos por segundo.
  - $\omega_0 = 2\pi f_0$: **Frecuencia angular** en radianes por segundo ($\text{rad/s}$).
  - $T_0 = \frac{1}{f_0} = \frac{2\pi}{\omega_0}$: **Periodo fundamental** en segundos ($\text{s}$). Condición: $x(t + T_0) = x(t)$.
  - $\phi$: **Fase inicial** en radianes ($\text{rad}$), desfase en $t = 0$.
  - $t$: **Tiempo continuo** ($\text{s}$).

### 2. Puntos importantes del seno y coseno en términos de $\pi$
- **Periodo base**: $2\pi \text{ rad} = 360^\circ$.
- **Tabla de valores clave**:
  | $\theta$ | $0$ | $\frac{\pi}{6}$ | $\frac{\pi}{4}$ | $\frac{\pi}{3}$ | $\frac{\pi}{2}$ | $\pi$ | $\frac{3\pi}{2}$ | $2\pi$ |
  | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
  | **Grados** | $0^\circ$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ | $180^\circ$ | $270^\circ$ | $360^\circ$ |
  | $\sin(\theta)$ | $0$ | $\frac{1}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{3}}{2}$ | $1$ | $0$ | $-1$ | $0$ |
  | $\cos(\theta)$ | $1$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{2}}{2}$ | $\frac{1}{2}$ | $0$ | $-1$ | $0$ | $1$ |
- **Relaciones de desfase y simetría**:
  - **Desfase relativo ($\frac{\pi}{2}$ rad / $90^\circ$)**: $\cos(\theta) = \sin\left(\theta + \frac{\pi}{2}\right)$ *(el coseno adelanta al seno en $\frac{\pi}{2}$)*; $\sin(\theta) = \cos\left(\theta - \frac{\pi}{2}\right)$.
  - **Inversión de signo ($\pi$ rad / $180^\circ$)**: $\sin(\theta \pm \pi) = -\sin(\theta)$, $\cos(\theta \pm \pi) = -\cos(\theta)$.
  - **Paridad**: $\sin(-\theta) = -\sin(\theta)$ (**función impar**); $\cos(-\theta) = \cos(\theta)$ (**función par**).

### 3. Frecuencia y periodo de varias señales senoidales sumadas
- **Frecuencia fundamental ($f_0$)**: **MCD** (Máximo Común Divisor) de las frecuencias individuales:
  $$f_0 = \text{MCD}(f_1, f_2, \dots, f_N)$$
- **Periodo fundamental ($T_0$)**: **MCM** (Mínimo Común Múltiplo) de los periodos individuales:
  $$T_0 = \text{MCM}(T_1, T_2, \dots, T_N)$$
- **Cálculo con fracciones**:
  - $\text{MCD}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\text{MCD}(a, c)}{\text{MCM}(b, d)}$
  - $\text{MCM}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\text{MCM}(a, c)}{\text{MCD}(b, d)}$