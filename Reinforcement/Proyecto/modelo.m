
A1 = pi/4;
A2 = pi/400;
ro = 1000;
g = 9.8;
k1 = -(A2*sqrt(2*g))/A1;
k2 = 1/(ro*A1);
Q_estrella = 34.77;
omega = (g*ro*A2^2)/(A1*Q_estrella);
csys = tf(k2,[1,omega]); % función de transferencia en continuo
ts = 0.2;
dsys=c2d(csys,ts,'z'); % sistema discreto
[num,den]=tfdata(dsys,'v');
disp(csys);
disp(dsys)

tiempo_total = 300;
its = tiempo_total/ts;

y = zeros(1,its);
t = zeros(1,its);
y(1) = 0; %altura inicial
u = Q_estrella;

for i=2:1:its
    y(i)=-den(2)*y(i-1)+num(2)*u;
    t(i) = ts*i;
end

plot(t, y);
