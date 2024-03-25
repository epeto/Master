
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Defining the model structure. We can define the network by just passing a list of edges.
model = BayesianNetwork([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

cpd_d_sn = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]], state_names={'D': ['Easy', 'Hard']})
cpd_i_sn = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]], state_names={'I': ['Dumb', 'Intelligent']})
cpd_g_sn = TabularCPD(variable='G', variable_card=3,
                      values=[[0.3, 0.05, 0.9,  0.5],
                              [0.4, 0.25, 0.08, 0.3],
                              [0.3, 0.7,  0.02, 0.2]],
                      evidence=['I', 'D'],
                      evidence_card=[2, 2],
                      state_names={'G': ['A', 'B', 'C'],
                                   'I': ['Dumb', 'Intelligent'],
                                   'D': ['Easy', 'Hard']})

cpd_l_sn = TabularCPD(variable='L', variable_card=2,
                      values=[[0.1, 0.4, 0.99],
                              [0.9, 0.6, 0.01]],
                      evidence=['G'],
                      evidence_card=[3],
                      state_names={'L': ['Bad', 'Good'],
                                   'G': ['A', 'B', 'C']})

cpd_s_sn = TabularCPD(variable='S', variable_card=2,
                      values=[[0.95, 0.2],
                              [0.05, 0.8]],
                      evidence=['I'],
                      evidence_card=[2],
                      state_names={'S': ['Bad', 'Good'],
                                   'I': ['Dumb', 'Intelligent']})

model.add_cpds(cpd_d_sn, cpd_i_sn, cpd_g_sn, cpd_l_sn, cpd_s_sn)
model.check_model()

# 40
# Printing a CPD with it's state names defined.
print(40)
print(model.get_cpds('G'))

# 41
print("\n41")
print(model.get_cardinality('G'))

# 44
# Getting the local independencies of a variable.
print("\n44")
print(model.local_independencies('G'))

# 45
# Getting all the local independencies in the network.
print("\n45")
print(model.local_independencies(['D', 'I', 'S', 'G', 'L']))

# 48
# Active trail: For any two variables A and B in a network if any change in A influences the values of B then we say
#               that there is an active trail between A and B.
# In pgmpy active_trail_nodes gives a set of nodes which are affected (i.e. correlated) by any
# change in the node passed in the argument.
print("\n48")
print(model.active_trail_nodes('D'))

# 49
print("\n49")
print(model.active_trail_nodes('D', observed='G'))

# 52
infer = VariableElimination(model)
g_dist = infer.query(['G'])
print("\n52")
print(g_dist)

# 58
print("\n58")
print(infer.query(['G'], evidence={'D': 'Easy', 'I': 'Intelligent'}))

# 59
print("\n59")
print(infer.map_query(['G']))

# 60
print("\n60")
print(infer.map_query(['G'], evidence={'D': 'Easy', 'I': 'Intelligent'}))

# 61
print("\n61")
print(infer.map_query(['G'], evidence={'D': 'Easy', 'I': 'Intelligent', 'L': 'Good', 'S': 'Good'}))

