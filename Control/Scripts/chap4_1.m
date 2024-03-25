
% Fuzzy control for water tank
close all;

%a = newfis('fuzz_tank');
a = mamfis();
%a = sugfis('fuzz_tank');

a = addInput(a, [-3 3], "Name", "e"); % Parameter e
%fis = addMF(fis,"speed","trapmf",[50 70 80 85],'Name',"high");
a = addMF(a, "e", "zmf", [-3 -1], "Name", "NB");
a = addMF(a, "e", "trimf", [-3 -1 1], "Name", "NS");
a = addMF(a, "e", "trimf", [-2 0 2], "Name", "Z");
a = addMF(a, "e", "trimf", [-1 1 3], "Name", "PS");
a = addMF(a, "e", "smf", [1 3], "Name", "PB");

a = addOutput(a, [-4 4], "Name", "u"); % Parameter u
a = addMF(a, "u", "zmf", [-4 -1], "Name", "NB");
a = addMF(a, "u", "trimf", [-4 -2 1], "Name", "NS");
a = addMF(a, "u", "trimf", [-2 0 2], "Name", "Z");
a = addMF(a, "u", "trimf", [-1 2 4], "Name", "PS");
a = addMF(a, "u", "smf", [1 4], "Name", "PB");

rulelist = [1, 1, 1, 1;
            2, 2, 1, 1;
            3, 3, 1, 1;
            4, 4, 1, 1;
            5, 5, 1, 1];

a = addRule(a, rulelist);
a.DefuzzificationMethod = 'mom';
writeFIS(a, 'tank');
a2 = readfis('tank');

figure(1);
plotfis(a2);
figure(2);
plotmf(a, 'input', 1);
figure(3);
plotmf(a, 'output', 1);

flag = 0; % cambiar bandera
if flag == 1
    showrule(a); % Show fuzzy rule base
    ruleview('tank'); % Dynamic simulation
end
disp('--------------------------------------------------');
disp('   fuzzy controller table: e=[-3,+3], u=[-4,+4]   ');
disp('--------------------------------------------------');

for i=1:1:7
    e(i) = i-4;
    Ulist(i) = evalfis([e(i)], a2);
end
Ulist = round(Ulist);
e=-3; %error
u = evalfis(e, a2); % Using fuzzy inference

%%%%%%%%%%%%%%%%%%%%%%%% Zona de funciones %%%%%%%%%%%%%%%%%%%%%%%%%%

function C = compound(A, B)
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

function C = union(A, B)
    sizeA = size(A);
    sizeB = size(B);
    if sizeA(1) ~= sizeB(1) || sizeA(2) ~= sizeB(2)
        C = zeros(1)
    else
        C = zeros(sizeA(1), sizeA(2));
        for i=1:sizeA(1)
            for j=1:sizeA(2)
                C(i,j) = max(A(i,j), B(i,j));
            end
        end
    end
end