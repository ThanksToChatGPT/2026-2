clear; clc; close all;

% Cargar audio
[y, Fs] = audioread('Grabacion.ogg');
y_inv = flipud(y)
%Fs = 100000
% Vector de tiempo
t = (0:length(y)-1) / Fs;

sound(y, Fs)

sound(y_inv, Fs)
% Graficar la señal
plot(t, y);
title('Señal de Voz');
xlabel('Tiempo (s)');
ylabel('Amplitud');
grid on;
