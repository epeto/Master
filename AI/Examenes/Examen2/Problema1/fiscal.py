
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = BayesianNetwork([('B', 'I'), ('B', 'G'), ('I', 'G'), ('M', 'I'), ('M', 'G'), ('G', 'J')])

cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.1], [0.9]])

cpd_m = TabularCPD(variable='M', variable_card=2, values=[[0.9], [0.1]])
                     
cpd_i = TabularCPD(variable='I', variable_card=2,
                   values=[[0.9, 0.5, 0.5, 0.1],
                           [0.1, 0.5, 0.5, 0.9]],
                   evidence=['B', 'M'],
                   evidence_card=[2, 2])
                   
cpd_g = TabularCPD(variable='G', variable_card=2,
                   values=[[1, 1, 0.9, 0.8, 1, 1, 0.2, 0.1],
                           [0, 0, 0.1, 0.2, 0, 0, 0.8, 0.9]],
                   evidence=['B', 'I', 'M'],
                   evidence_card=[2, 2, 2])

cpd_j = TabularCPD(variable='J', variable_card=2,
                      values=[[1, 0.1],
                              [0, 0.9]],
                      evidence=['G'],
                      evidence_card=[2])


model.add_cpds(cpd_b, cpd_m, cpd_i, cpd_g, cpd_j)
model.check_model()

# P(Burglary | JohnCalls =true, MaryCalls =true)
infer = VariableElimination(model)
# print(infer.query(['B'], evidence={'J': 1, 'M': 1}))
print(infer.query(['J'], evidence={'G':0, 'I':0}))
print(infer.query(['J'], evidence={'G':0, 'I':1}))
print(infer.query(['J'], evidence={'G':1, 'I':0}))
print(infer.query(['J'], evidence={'G':1, 'I':1}))


