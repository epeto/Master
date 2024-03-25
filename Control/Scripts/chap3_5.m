close all;

A=[0.5;1;0.1];
B=[0.1,1,0.6];
C=[0.4,1];

% Compound of A and B
AB = compound(A,B);
% Transfer to column
T1 = [];
for i=1:3
    T1 = [T1;AB(i,:)'];
end

% Get fuzzy R
R = compound(T1, C);
disp("R:");
disp(R);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A1 = [1; 0.5; 0.1];
B1 = [0.1, 0.5, 1];

AB1 = compound(A1,B1);

% Transfer to row
T2 = [];
for i=1:3
    T2 = [T2, AB1(i,:)];
end

% Get output C1
C1 = compound(T2, R);
disp("C1:");
disp(C1);

%%%%%%%%%%%%%%%%%%%%%%%% Zona de funciones %%%%%%%%%%%%%%%%%%%%%%%%%%

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
