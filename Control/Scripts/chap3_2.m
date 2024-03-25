% Funciones de pertenencia
close all;

disp("1.-Gausiana");
disp("2.-Campana general");
disp("3.-S");
disp("4.-Trapezoide")
disp("5.-Triángulo");
disp("6.-Z");
prompt = "Introduzca un valor del 1 al 6\n";
M = input(prompt);
x=0:0.1:10;
if M==1 % Gausiana
    y=gaussmf(x,[2 5]);
elseif M==2 % General bell
    y=gbellmf(x,[2 4 6]);
elseif M==3 % S
    y=sigmf(x,[2 4]);
elseif M==4 % Trapezoide
    y=trapmf(x,[1 5 7 8]);
elseif M==5 % Triángulo
    y=trimf(x, [3 6 8]);
elseif M==6 % Z
    y=zmf(x, [3 7]);
end

if 1<=M && M<=6
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
end