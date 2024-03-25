
% Parte 1: generación del sistema de inferencia borroso
close all;

% Basado en el script 1 del capítulo 4 (tanque de agua)
a = mamfis();

a = addInput(a, [-3 3], "Name", "e"); % e
a = addMF(a, "e", "zmf", [-3 -1], "Name", "NB");
a = addMF(a, "e", "trimf", [-3 -1 1], "Name", "NS");
a = addMF(a, "e", "trimf", [-2 0 2], "Name", "Z");
a = addMF(a, "e", "trimf", [-1 1 3], "Name", "PS");
a = addMF(a, "e", "smf", [1 3], "Name", "PB");

a = addOutput(a, [-4 4], "Name", "u"); % u
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
a.DefuzzificationMethod = "mom";
writeFIS(a, 'tank');
