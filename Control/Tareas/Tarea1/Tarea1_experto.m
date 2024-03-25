
% Experto
% clear all;
close all;
ts=0.1;
sys = tf(3000,[1,150,1000,500]); %Planta
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;u_3=0;u_4=0;
y_1=0;y_2=0;y_3=0;
ei=0;
error_1=0;error_2=0;derror_1=0;

kp = 0.5;
ki = 0.2;
kd = 0.05;

k1 = 1.95;
k2 = 0.45;
M1_1 = 0.8;
M1_2 = 0.6;
M1_3 = 0.4;
M1_4 = 0.01;
M2 = 0.08;
epsilon = 0.001;

sz = 50; %número de iteraciones
time = zeros(1,sz);
yd = zeros(1,sz);
y = zeros(1,sz);
error = zeros(1,sz);
derror = zeros(1,sz);
u = zeros(1,sz);

for k=1:1:sz
    time(k)=k*ts;
    yd(k)=1.0;
    % Linear model
    y(k) = -den(2)*y_1 - den(3)*y_2 - den(4)*y_3 + num(1)*u_1 + num(2)*u_2 + num(3)*u_3 + num(4)*u_4;
    error(k)=yd(k)-y(k); % Calculating P
    derror(k)=error(k)-error_1; % Calculating D
    ei=ei+error(k)*ts; % Calculating I
    u(k)=kp*error(k) + (kd*derror(k))/ts + ki*ei; %tradicional
    
    % Expert control rule
    % Rule1:Unclosed control rule
    if abs(error(k)) > M1_1
        u(k) = 0.5;
    elseif abs(error(k)) > M1_2
        u(k) = 0.3;
    elseif abs(error(k)) > M1_3
        u(k) = 0.1;
    elseif abs(error(k)) > M1_4
        u(k) = 0.1;
    end

    % Rule 2
    if error(k)*derror(k)>0 || derror(k)==0
        if abs(error(k)) >= M2
            %control fuerte
            %u(k) = u_1 + k1*(kp*(error(k)-error_1) + ki*error(k) + kd*(error(k)-2*error_1+error_2));
            u(k) = u_1 + 1.6*kp*error(k);
        else
            %control débil
            %u(k) = u_1 + kp*(error(k)-error_1) + ki*error(k) + kd*(error(k)-2*error_1+error_2);
            u(k) = u_1 + 0.35*kp*error(k);
        end
    end

    % Rule 3
    if (error(k)*derror(k)<0 && derror(k)*derror_1>0) || (error(k)==0)
        %u(k) = 1.65*u(k);
        u(k) = u_1;
    end

    % Rule 4
    if error(k)*derror(k)<0 && derror(k)*derror_1<0
        if abs(error(k)) >= M2
            u(k)=u_1 + k1*kp*error(k);
        else
            u(k)=u_1 + k2*kp*error(k);
        end
    end

    % Rule5:Integration separation PI control
    if (abs(error(k)) <= epsilon)
        u(k)=0.4*error(k)+0.01*ei;
    end

    u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
    y_3=y_2;y_2=y_1;y_1=y(k);
    error_2=error_1;error_1=error(k);
    derror_1=derror(k);
end


figure(1);
plot(time,yd,'r',time,y,'b:','linewidth',2);
xlabel('time(s)');ylabel('r,y');
legend('Ideal position','Practical position');
figure(2);
plot(time,yd-y,'r','linewidth',2);
xlabel('time(s)');ylabel('error');

