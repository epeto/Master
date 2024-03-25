
% Control borroso de tanque de agua.
% Parte 2: control
close all;

fis = readfis('tank'); % se lee el archivo
ts = 0.05; % periodo en segundos
sys = tf(20, [1, 1]); % planta
dsys = c2d(sys, ts, 'z');
[num, den] = tfdata(dsys, 'v');

% valores iniciales [1.5, 0.5, 3]
nivel_inicial = 2.7;
nivel_ideal = 1;

Q0 = 0.05;

% creación de arreglos de manera estática
iter = 1000; % número total de iteraciones
time = zeros(1,iter);
yd = ones(1, iter);
u = zeros(1, iter);
y = zeros(1, iter);
e = zeros(1, iter);

y(1) = nivel_inicial;
e(1) = yd(1) - y(1);
u(1) = Q0;

for k=2:iter
    time(k) = k*ts;
    e(k) = yd(k) - y(k-1);
    u(k) = evalfis(fis, e(k));
    y(k) = - den(2)*y(k-1) + num(2)*u(k-1);
end

figure(1);
plot(time, yd, 'r', time, y, 'b:', 'linewidth', 2);
xlabel('time(s)'); ylabel('r,y');
legend('Ideal position', 'Practical position');

figure(2);
plot(time, u, 'r', 'linewidth', 2);
xlabel('time(s)');
ylabel('Control input');
