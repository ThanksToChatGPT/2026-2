% Problema 1: Álgebra de Números Complejos

% Crear los números complejos z_1 y z_2
z1 = 2 - 1j;
z2 = 3 + 6j;

% Solucionar la ecuación: z2^2 + x = -z1^2  =>  x = -z1^2 - z2^2
x = -z1^2 - z2^2;

% Imprimir resultado
fprintf('dado z_1 = %s y z_2 = %s el x que cumple la ecuacion es: %s\n', num2str(z1), num2str(z2), num2str(x));


%% Problema 2: Trayectoria de una Función Compleja Parametrizada
% Intervalo de tiempo t en [0, 4*pi]
t = linspace(0, 4*pi, 1000);

% Función compleja Z(t) = t * e^(j*t)
Z = t .* exp(1j * t);

% Gráfica en el plano complejo (Re{Z} vs. Im{Z}) de manera sencilla
figure;
plot(real(Z), imag(Z), 'b', 'LineWidth', 1.5);
grid on;
axis equal;
xlabel('Re\{Z(t)\}');
ylabel('Im\{Z(t)\}');
title('Problema 2: Trayectoria de Z(t) = t \cdot e^{jt}');


%% Problema 3: Representación Gráfica de Funciones Especiales
% Parámetros de la función compleja z(t) = exp((alpha + 1j*omega)*t)
alpha = -0.5;
omega = 2*pi;

% Intervalo de tiempo t en [0, 5] segundos
t3 = linspace(0, 5, 2000);

% Función compleja z(t)
z3 = exp((alpha + 1j*omega) * t3);

% Gráfica de la trayectoria en el plano complejo (Re{z} vs. Im{z})
figure;
plot(real(z3), imag(z3), 'r', 'LineWidth', 1.5);
grid on;
axis equal;
xlabel('Re\{z(t)\}');
ylabel('Im\{z(t)\}');
title('Problema 3: Trayectoria de z(t) = e^{(-0.5 + j2\pi)t}');


%% Problema 4: Raíces n-ésimas de la Unidad
% Cálculo de las raíces sextas de la unidad: z^6 = 1
n = 6;
k = 0:(n-1);
raices = exp(1j * 2 * pi * k / n);

% Gráfica en el plano complejo
figure;
theta_circ = linspace(0, 2*pi, 300);
plot(cos(theta_circ), sin(theta_circ), 'k--', 'LineWidth', 1); % Circunferencia unitaria
hold on;
plot([real(raices) real(raices(1))], [imag(raices) imag(raices(1))], 'b-', 'LineWidth', 1.2); % Hexágono
plot(real(raices), imag(raices), 'ro', 'MarkerFaceColor', 'r', 'MarkerSize', 8); % Raíces
grid on;
axis equal;
xlabel('Re\{z\}');
ylabel('Im\{z\}');
title('Problema 4: Raíces sextas de la unidad (z^6 = 1)');
legend('Circunferencia unitaria', 'Polígono regular (Hexágono)', 'Raíces z_k', 'Location', 'best');
hold off;


%% Problema 5: Rotación y Superposición de Fasores
% Parámetros de las señales armónicas
t5 = linspace(0, 2, 2000); % Tiempo para 2 períodos
u1 = (4/pi) * sin(2*pi*t5);
u2 = (4/(3*pi)) * sin(6*pi*t5);
u3 = (4/(5*pi)) * sin(10*pi*t5);
u = u1 + u2 + u3; % Onda resultante (aproximación cuadrada)

% Instante de observación para el brazo articulado
t0 = 0.12; % segundos
v1 = (4/pi) * exp(1j * 2*pi * t0);
v2 = v1 + (4/(3*pi)) * exp(1j * 6*pi * t0);
v3 = v2 + (4/(5*pi)) * exp(1j * 10*pi * t0);

figure('Position', [100, 100, 1000, 450]);

% Panel 1: Rotación y superposición fasorial en el plano complejo
subplot(1, 2, 1);
theta = linspace(0, 2*pi, 300);
% Circunferencias de giro (epiciclos)
plot(real(v1) + (4/(3*pi))*cos(theta), imag(v1) + (4/(3*pi))*sin(theta), 'r:', 'LineWidth', 1);
hold on;
plot(real(v2) + (4/(5*pi))*cos(theta), imag(v2) + (4/(5*pi))*sin(theta), 'k:', 'LineWidth', 1);
% Trayectoria de la punta U(t)
Ut = (4/pi)*exp(1j*2*pi*t5) + (4/(3*pi))*exp(1j*6*pi*t5) + (4/(5*pi))*exp(1j*10*pi*t5);
plot(real(Ut), imag(Ut), 'Color', [0.85 0.85 0.85], 'LineWidth', 1);
% Vectores del brazo articulado en t0
plot([0 real(v1)], [0 imag(v1)], 'b-', 'LineWidth', 2);
plot([real(v1) real(v2)], [imag(v1) imag(v2)], 'r-', 'LineWidth', 2);
plot([real(v2) real(v3)], [imag(v2) imag(v3)], 'k-', 'LineWidth', 2);
plot(real(v3), imag(v3), 'mo', 'MarkerFaceColor', 'm', 'MarkerSize', 6);
% Línea horizontal de proyección hacia el dominio temporal
plot([real(v3) 2.2], [imag(v3) imag(v3)], 'm--', 'LineWidth', 1.5);
grid on; axis equal; xlim([-2 2.2]); ylim([-1.8 1.8]);
xlabel('Re\{U(t)\}'); ylabel('Im\{U(t)\} (Altura)');
title('Plano Complejo: Articulación Fasorial');
legend('Epiciclo 2', 'Epiciclo 3', 'Trayectoria punta', ...
       'Fasor 1', 'Fasor 2', 'Fasor 3', 'Location', 'southwest');

% Panel 2: Proyección de la onda en el dominio del tiempo
subplot(1, 2, 2);
plot(t5, u, 'b-', 'LineWidth', 2); hold on;
plot(t5, u1, 'b--', 'LineWidth', 0.8);
plot(t0, imag(v3), 'mo', 'MarkerFaceColor', 'm', 'MarkerSize', 6);
plot([0 t0], [imag(v3) imag(v3)], 'm--', 'LineWidth', 1.5);
grid on; xlim([0 2]); ylim([-1.8 1.8]);
xlabel('Tiempo t (s)'); ylabel('u(t) = \Sigma u_k(t)');
title('Dominio del Tiempo: Onda Cuadrada Reconstruida');
legend('u(t) Resultante (3 armónicos)', 'u_1(t) Fundamental', ...
       'Punto proyectado', 'Location', 'northeast');
