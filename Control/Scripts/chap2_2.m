%Expert PID Controller
%clear all;
close all;
ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]); %Plant
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;u_3=0;u_4=0;
y_1=0;y_2=0;y_3=0;
ei=0;
error_1=0;derror_1=0;
kp=0.6;ki=0.03;kd=0.01;

time = zeros(1,500);
yd = zeros(1,500);
y = zeros(1,500);
error = zeros(1,500);
derror = zeros(1,500);
u = zeros(1,500);

for k=1:1:500
    time(k)=k*ts;
    yd(k)=1.0;
    % Linear model
    y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(1)*u_1+num(2)*u_2+num(3)*u_3+num(4)*u_4;
    error(k)=yd(k)-y(k); % Calculating P
    derror(k)=error(k)-error_1; % Calculating D
    ei=ei+error(k)*ts; % Calculating I
    u(k)=kp*error(k)+kd*derror(k)/ts+ki*ei; %PID Controller
    
    % Expert control rule
    % Rule1:Unclosed control rule
    if abs(error(k))>0.8
        u(k)=0.45;
    elseif abs(error(k))>0.40
        u(k)=0.40;
    elseif abs(error(k))>0.20
        u(k)=0.12;
    elseif abs(error(k))>0.01
        u(k)=0.10;
    end

    % Rule 2
    if error(k)*derror(k)>0 || (derror(k)==0)
        if abs(error(k))>=0.05
            u(k)=u_1+2*kp*error(k);
        else
            u(k)=u_1+0.4*kp*error(k);
        end
    end

    % Rule3
    if (error(k)*derror(k)<0 && derror(k)*derror_1>0) || (error(k)==0)
        u(k) = u(k);
    end

    % Rule4
    if error(k)*derror(k)<0 && derror(k)*derror_1<0
        if abs(error(k))>=0.05
            u(k)=u_1+2*kp*error(k);
        else
            u(k)=u_1+0.6*kp*error(k);
        end
    end

    % Rule5:Integration separation PI control
    if abs(error(k))<=0.001
        u(k)=0.5*error(k)+0.010*ei;
    end

    u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
    y_3=y_2;y_2=y_1;y_1=y(k);
    error_1=error(k);
    derror_1=derror(k);
end

figure(1);
plot(time,yd,'r',time,y,'b:','linewidth',2);
xlabel('time(s)');ylabel('r,y');
legend('Ideal position','Practical position');
figure(2);
plot(time,yd-y,'r','linewidth',2);
xlabel('time(s)');ylabel('error');
