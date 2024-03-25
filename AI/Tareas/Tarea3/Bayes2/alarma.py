
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('B', 'A'), ('E', 'A'), ('A', 'J'), ('A', 'M')])

cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.999], [0.001]])

cpd_e = TabularCPD(variable='E', variable_card=2, values=[[0.998], [0.002]])

cpd_a = TabularCPD(variable='A', variable_card=2,
                      values=[[0.999, 0.71, 0.06, 0.05],
                              [0.001, 0.29, 0.94, 0.95]],
                      evidence=['B', 'E'],
                      evidence_card=[2, 2])

cpd_j = TabularCPD(variable='J', variable_card=2,
                      values=[[0.95, 0.1],
                              [0.05, 0.9]],
                      evidence=['A'],
                      evidence_card=[2])

cpd_m = TabularCPD(variable='M', variable_card=2,
                      values=[[0.99, 0.3],
                              [0.01, 0.7]],
                      evidence=['A'],
                      evidence_card=[2])

model.add_cpds(cpd_b, cpd_e, cpd_a, cpd_j, cpd_m)
model.check_model()

# P(Burglary | JohnCalls =true, MaryCalls =true)
infer = VariableElimination(model)
print("P(B | J=1, M=1)")
print(infer.query(['B'], evidence={'J': 1, 'M': 1}))

