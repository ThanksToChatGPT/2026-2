# Señales Elementales

### 1. Escalón Unitario

$$u(t) = \begin{cases} 0, & t \le 0 \\ 1, & t > 0 \end{cases}$$

![Escalón Unitario](img/escalon.png)

---

### 2. Pulso Rectangular

$$\operatorname{rect}\left(\frac{t}{T}\right) = \Pi\left(\frac{t}{T}\right) = \begin{cases} 1, & |t| < \frac{T}{2} \\ 0, & |t| > \frac{T}{2} \end{cases}$$

> Pulso de ancho $T$, centrado en el origen (desde $-\frac{T}{2}$ hasta $\frac{T}{2}$).

![Pulso Rectangular](img/rectangular.png)

---

### 3. Pulso Triangular

$$\operatorname{tri}\left(\frac{t}{T}\right) = \Lambda\left(\frac{t}{T}\right) = \begin{cases} \frac{t}{T} + 1, & -T \le t < 0 \\ -\frac{t}{T} + 1, & 0 \le t \le T \\ 0, & \text{en otro caso} \end{cases}$$

![Pulso Triangular](img/triangular.png)

---

### 4. Función Rampa

$$r(t) = \begin{cases} t, & t > 0 \\ 0, & t \le 0 \end{cases}$$

![Función Rampa](img/rampa.png)

---

### 5. Función Sinc

$$\operatorname{sinc}(t) = \frac{\sin(\pi t)}{\pi t}$$

![Función Sinc](img/sinc.png)

---

### 6. Delta de Dirac (Impulso Unitario)

$$\delta(t) = \begin{cases} \infty, & t = 0 \\ 0, & t \ne 0 \end{cases}$$

**Propiedades fundamentales:**
* **Área unitaria:**
  $$\int_{-\infty}^{\infty} \delta(t) \, dt = 1$$
* **Propiedad de muestreo (tamizado):**
  $$x(t)\delta(t - t_0) = x(t_0)\delta(t - t_0)$$
* **Relación con el escalón unitario:**
  $$\int_{-\infty}^{t} \delta(\tau) \, d\tau = u(t)$$

![Delta de Dirac](img/dirac.png)

---

### 7. Señal Exponencial Compleja

$$x(t) = A e^{j(\omega_0 t + \theta)}$$

Por la fórmula de Euler:
$$x(t) = A\cos(\omega_0 t + \theta) + j A\sin(\omega_0 t + \theta)$$

* **Parte Real:** $\operatorname{Re}\{x(t)\} = A\cos(\omega_0 t + \theta)$
* **Parte Imaginaria:** $\operatorname{Im}\{x(t)\} = A\sin(\omega_0 t + \theta)$
* **Periodo fundamental:** $T_0 = \frac{2\pi}{\omega_0}$

![Exponencial Compleja](img/exponencial_compleja.png)
---

### 8. Señales de Energía y Potencia

* **Potencia Instantánea:**
  $$p(t) = |x(t)|^2$$

* **Energía Total ($E$):**
  $$E = \int_{-\infty}^{\infty} |x(t)|^2 \, dt$$

* **Potencia Media ($P$):**
  $$P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 \, dt$$

  > Para señales periódicas de periodo fundamental $T_0$:
  > $$P = \frac{1}{T_0} \int_{T_0} |x(t)|^2 \, dt$$

**Clasificación:**
* **Señal de Energía:** $0 < E < \infty \implies P = 0$ *(típicamente pulsos y señales aperiódicas)*.
* **Señal de Potencia:** $0 < P < \infty \implies E = \infty$ *(típicamente señales periódicas continuas)*.
* Una señal **no puede ser de ambas clases a la vez**, y existen señales que no pertenecen a ninguna de las dos.