
% Modelo de Takagi-Sugeno del error del tanque

close all;

ts = sugfis();
ts = addInput(ts, [-2 2], 'Name', 'error'); % entrada: error
ts = addMF(ts, 'error', 'zmf', [-1 -0.75], 'Name', 'NB'); % negative big
ts = addMF(ts, 'error', 'gaussmf', [0.25 -0.75], 'Name', 'NM'); % negative medium
ts = addMF(ts, 'error', 'gaussmf', [0.2 -0.3], 'Name', 'NS'); % negative small
ts = addMF(ts, 'error', 'gaussmf', [0.1 0], 'Name', 'Z'); % zero
ts = addMF(ts, 'error', 'gaussmf', [0.2 0.3], 'Name', 'PS'); % positive small
ts = addMF(ts, 'error', 'gaussmf', [0.25 0.75], 'Name', 'PM'); % positive medium
ts = addMF(ts, 'error', 'smf', [0.75 1], 'Name', 'PB'); % positive big

ts = addOutput(ts, [0 1], 'Name', 'V1'); % salida 1: V1
ts = addMF(ts, 'V1', 'constant', 0, 'Name', 'FDR'); % fuera de rango
ts = addMF(ts, 'V1', 'constant', 0.25, 'Name', 'Z'); % cerca del cero
ts = addMF(ts, 'V1', 'constant', 0.5, 'Name', 'S'); % small
ts = addMF(ts, 'V1', 'constant', 0.75, 'Name', 'M'); % medium
ts = addMF(ts, 'V1', 'constant', 1, 'Name', 'B'); % big

ts = addOutput(ts, [0 1], 'Name', 'V2'); % salida 2: V2
ts = addMF(ts, 'V2', 'constant', 0, 'Name', 'FDR'); % fuera de rango
ts = addMF(ts, 'V2', 'constant', 0.25, 'Name', 'Z'); % cerca del cero
ts = addMF(ts, 'V2', 'constant', 0.5, 'Name', 'S'); % small
ts = addMF(ts, 'V2', 'constant', 0.75, 'Name', 'M'); % medium
ts = addMF(ts, 'V2', 'constant', 1, 'Name', 'B'); % big

% definir reglas
reglas(1) = "error == NB => V1 = FDR, V2 = B";
reglas(2) = "error == NM => V1 = FDR, V2 = M";
reglas(3) = "error == NS => V1 = FDR, V2 = S";
reglas(4) = "error == Z => V1 = Z, V2 = Z";
reglas(5) = "error == PS => V1 = S, V2 = FDR";
reglas(6) = "error == PM => V1 = M, V2 = FDR";
reglas(7) = "error == PB => V1 = B, V2 = FDR";
ts = addRule(ts, reglas);

writeFIS(ts, 'error_tanque');
figure(1);
plotmf(ts, 'input', 1);
figure(2);
plotfis(ts);

