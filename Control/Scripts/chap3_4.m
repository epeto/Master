
close all;

A=[0.8, 0.7;
   0.5, 0.3];
B=[0.2, 0.4;
   0.6, 0.9];

dimens = size(A);
filas = dimens(1);
columnas = dimens(2);
n = filas; % En este caso se puede hacer porque son cuadradas

% Composición de A y B
AB = compound(A, B);
disp(AB);

% Composición de B y A
BA = compound(B, A);
disp(BA);

function C=compound(A,B)
    sizeA = size(A);
    sizeB = size(B);
    if sizeA(2) ~= sizeB(1)
        C = zeros(1);
    else
        filasA = sizeA(1);
        columnasB = sizeB(2);
        C = zeros(filasA, columnasB);
        rangoK = sizeA(2);
        for i=1:filasA
            for j=1:columnasB
                for k=1:rangoK
                    minab = min(A(i,k), B(k,j));
                    C(i,j) = max(C(i,j), minab);
                end
            end
        end
    end
end