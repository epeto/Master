% Fuzzy tuning PI control
close all;

a = mamfis();
a = addInput(a, [-1 1], 'Name', 'e'); % Parameter e
a = addMF(a, 'e', 'zmf', [-1, -1/3], 'Name', 'N');
a = addMF(a, 'e', 'trimf', [-2/3, 0, 2/3], 'Name', 'Z');
a = addMF(a, 'e', 'smf', [1/3, 1], 'Name', 'P');

a = addInput(a, [-1 1], 'Name', 'ec'); % Parameter ec
a = addMF(a, 'ec', 'zmf', [-1, -1/3], 'Name', 'N');
a = addMF(a, 'ec', 'trimf', [-2/3, 0, 2/3], 'Name', 'Z');
a = addMF(a, 'ec', 'smf', [1/3, 1], 'Name', 'P');

a = addOutput(a, (1/3)*[-10 10], 'Name', 'kp');
a = addMF(a, 'kp', 'zmf', (1/3)*[-10, -3], 'Name', 'N');
a = addMF(a, 'kp', 'trimf', (1/3)*[-5, 0, 5], 'Name', 'Z');
a = addMF(a, 'kp', 'smf', (1/3)*[3, 10], 'Name', 'P');

a = addOutput(a, (1/30)*[-3 3], 'Name', 'ki');
a = addMF(a, 'ki', 'zmf', (1/30)*[-3, -1], 'Name', 'N');
a = addMF(a, 'ki', 'trimf', (1/30)*[-2, 0, 2], 'Name', 'Z');
a = addMF(a, 'ki', 'smf', (1/30)*[1, 3], 'Name', 'P');

rulelist = [1 1 1 2 1 1;
            1 2 1 2 1 1;
            1 3 1 2 1 1;
            2 1 1 3 1 1;
            2 2 3 3 1 1;
            2 3 3 3 1 1;
            3 1 3 2 1 1;
            3 2 3 2 1 1;
            3 3 3 2 1 1];

a = addRule(a, rulelist);
a = setfis(a, 'DefuzzMethod', 'centroid');
writeFIS(a, 'fuzzpid');

a = readfis('fuzzpid');
figure(1);
plotmf(a, 'input', 1);
figure(2);
plotmf(a, 'input', 2);
figure(3);
plotmf(a, 'output', 1);
figure(4);
plotmf(a, 'output', 2);
figure(5);
plotfis(a);
fuzzy fuzzpid;
showrule(a);
ruleview fuzzpid;

