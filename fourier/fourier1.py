import numpy as np
import matplotlib.pyplot as plt


T=2;

fs=128;

t=[0:1/fs:T];

N=length(t);
f=sin(10*2*pi*t)+sin(20*2*pi*t);

g=f+randn(size(f));

F=fft(f)/sqrt(N);

G=fft(g)/sqrt(N);


omega=0.5*fs*linspace(0,1,floor(N/2)+1); % vector de frecuencias discretas
range=(1:floor(N/2)+1);

P=F(range).*conj(F(range));

Q=G(range).*conj(G(range));

figure, plot(omega,P), xlabel('frequency'), ylabel('P'),title('Espectro de potencia de la señal f')
figure, plot(omega,Q), xlabel('frequency'), ylabel('Q'),title('Espectro de potencia de la señal g')