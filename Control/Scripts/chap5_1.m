% T-S type fuzzy model
close all;

ts2 = sugfis();
ts2 = addInput(ts2, [0 5], 'Name', 'X');
ts2 = addMF(ts2, 'X', 'gaussmf', [1.8 0], 'Name', 'little');
ts2 = addMF(ts2, 'X', 'gaussmf', [1.8 5], 'Name', 'big');

ts2 = addInput(ts2, [0 10], 'Name', 'Y');
ts2 = addMF(ts2, 'Y', 'gaussmf', [4.4 0], 'Name', 'little');
ts2 = addMF(ts2, 'Y', 'gaussmf', [4.4 10], 'Name', 'big');

ts2 = addOutput(ts2, [-3 15], 'Name', 'Z');
ts2 = addMF(ts2, 'Z', 'linear', [-1 1 -3], 'Name', 'first area');
ts2 = addMF(ts2, 'Z', 'linear', [1 1 1], 'Name', 'second area');
ts2 = addMF(ts2, 'Z', 'linear', [0 -2 2], 'Name', 'third area');
ts2 = addMF(ts2, 'Z', 'linear', [2 1 -6], 'Name', 'fourth area');

rulelist=[1 1 1 1 1;
          1 2 2 1 1;
          2 1 3 1 1;
          2 2 4 1 1];

ts2 = addRule(ts2, rulelist);
showrule(ts2);
figure(1);
subplot 211;
plotmf(ts2, 'input', 1);
xlabel('x');
ylabel('MF Degree of input 1');
subplot 212;
plotmf(ts2, 'input', 2);
xlabel('x');
ylabel('Mf Degree of input 2');
figure(2);
gensurf(ts2);
xlabel('x');
ylabel('y');
zlabel('z');

