% Fuzzy control for washer
close all;

a = mamfis();
a = addInput(a, [0 100], "Name", "x"); % Fuzzy Stain
a = addMF(a, "x", "trimf", [0 0 50], "Name", "SD");
a = addMF(a, "x", "trimf", [0 50 100], "Name", "MD");
a = addMF(a, "x", "trimf", [50 100 100], "Name", "LD");

a = addInput(a, [0 100], "Name", "y"); % Fuzzy Axunge
a = addMF(a, "y", "trimf", [0 0 50], "Name", "NG");
a = addMF(a, "y", "trimf", [0 50 100], "Name", "MG");
a = addMF(a, "y", "trimf", [50 100 100], "Name", "LG");

a = addOutput(a, [0 60], "Name", "z"); % Fuzzy time
a = addMF(a, "z", "trimf", [0 0 10], "Name", "VS");
a = addMF(a, "z", "trimf", [0 10 25], "Name", "S");
a = addMF(a, "z", "trimf", [10 25 40], "Name", "M");
a = addMF(a, "z", "trimf", [25 40 60], "Name", "L");
a = addMF(a, "z", "trimf", [40 60 60], "Name", "VL");

rulelist = [1 1 1 1 1;
            1 2 3 1 1;
            1 3 4 1 1;
            2 1 2 1 1;
            2 2 3 1 1;
            2 3 4 1 1;
            3 1 3 1 1;
            3 2 4 1 1;
            3 3 5 1 1];

a = addRule(a, rulelist);
showrule(a); % show fuzzy rule base

a1 = setfis(a, 'DefuzzMethod', 'mom'); % Defuzzy
writeFIS(a1, 'wash');
a2 = readfis("wash");

figure(1);
plotfis(a2);
figure(2);

plotmf(a, 'input', 1);
figure(3);
plotmf(a, 'input', 2);
figure(4);
plotmf(a, 'output', 1);

ruleview('wash'); % Dynamic simulation

x = 60;
y = 70;
z = evalfis([x, y], a2); % using fuzzy inference
