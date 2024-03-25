
% BP approximation

%clear all;
close all;

xite = 0.5;
alfa = 0.05;

wjo = rands(6,1);
wjo_1 = wjo;
wjo_2 = wjo_1;

wij = rands(2,6);
wij_1 = wij;
wij_2 = wij;

dwij = 0*wij;
x = [0,0].';
u_1 = 0;
q_1 = 0;

I = [0,0,0,0,0,0].';
Iout = [0,0,0,0,0,0].';
FI = [0,0,0,0,0,0].';

ts = 0.001; % periodo
for k=1:1:1000
    time(k) = k*ts;
    u(k) = sin(pi*0.1*(k-1)*ts);
    q(k) = alfa*q_1^2 + u(k);
    x(1) = u(k);
    x(2) = q(k);
    for j=1:1:6
        I(j) = x.'*wij(:,j);
        Iout(j) = 1/(1+exp(-I(j)));
    end
    qo(k) = wjo.'*Iout; % Output of NNI networks
    e(k) = q(k) - qo(k); % Error calculation
    wjo = wjo_1 + (xite*e(k))*Iout + alfa*(wjo_1 - wjo_2);
    for j=1:1:6
        FI(j) = exp(-I(j))/(1+exp(-I(j)))^2;
    end
    
    for i=1:1:2
        for j=1:1:6
            dwij(i,j) = e(k)*xite*FI(j)*wjo(j)*x(i);
        end
    end
    wij = wij_1 + dwij + alfa*(wij_1 - wij_2);

    %%%%%%% Jacobian %%%%%%%%%%%%%
    qu = 0;
    for j=1:1:6
        qu = qu + wjo(j)*wij(1,j)*FI(j);
    end
    dqu(k) = qu;
    wij_2 = wij_1;
    wij_1 = wij;
    wjo_2 = wjo_1;
    wjo_1 = wjo;
    u_1 = u(k);
    q_1 = q(k);
end

figure(1);
plot(time, q, 'r', time, qo, 'b');
xlabel('times');
ylabel('q and qo');
figure(2);
plot(time, q-qo, 'r');
xlabel('times');
ylabel('error');
figure(3);
plot(time, dqu);
xlabel('times');
ylabel('dqu');

