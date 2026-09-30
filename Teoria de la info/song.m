% Melodía: Seven Nation Army - The White Stripes
n = 0.35; % negra
c = 0.15; % corchea
b = 0.70; % blanca
L = 1.00; % nota larga

partitura = {
    'mi', n; 'mi', c; 'sol', n; 'mi', n; 're', n; 'do', b; 'si', b;
    'mi', n; 'mi', c; 'sol', n; 'mi', n; 're', n; 'do', n; 're', n; 'do', n; 'si', L;
    'mi', n; 'mi', c; 'sol', n; 'mi', n; 're', n; 'do', b; 'si', L;
    'mi', n; 'mi', c; 'sol', n; 'mi', n; 're', n; 'do', n; 're', n; 'do', n; 'si', L
    };

for i = 1:size(partitura, 1)
    sonar_nota(partitura{i, 1}, partitura{i, 2});
    pause(0.02); 
end

function sonar_nota(nota, tiempo)
switch lower(nota)
    case 'do',  Hz = 261.63;
    case 're',  Hz = 293.66;
    case 'mi',  Hz = 329.63;
    case 'fa',  Hz = 349.23;
    case 'sol', Hz = 392.00;
    case 'la',  Hz = 440.00;
    case 'si',  Hz = 493.88;
    otherwise,  return;
end
sonar_frecuencia(Hz, tiempo);
end

function sonar_frecuencia(Hz, tiempo)
Fs = 44100;
t = 0:1/Fs:tiempo;
sound(sin(2 * pi * Hz * t), Fs);
pause(tiempo);
end