
import argparse
import gymnasium as gym
import torch.nn as nn
import torch
import numpy as np
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, num_inputs, num_actions):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(num_inputs, 32)
        self.fc2 = nn.Linear(32, 32)
        self.out = nn.Linear(32, num_actions)

    def forward(self, states):
        x = F.relu(self.fc1(states))
        x = F.relu(self.fc2(x))
        return self.out(x)

actions_continuous = np.linspace(-3.0, 3.0, num=100)

def epsilon_greedy(state, epsilon, env, main_nn):
    result = np.random.uniform()
    if result < epsilon:
        return random.randint(0, actions_continuous.shape[0]-1) # acción aleatoria
    else:
        qs = main_nn(torch.tensor(state, dtype=torch.float32)).cpu().data.numpy()
        return np.argmax(qs) # acción greedy

def d2c(idx):
    return torch.tensor([actions_continuous[idx]], dtype=torch.float32)
        
def main():
    env = gym.make('InvertedPendulum-v4', render_mode='human')
    observation, info = env.reset()
    modelo = DQN(env.observation_space.shape[0], len(actions_continuous))
    modelo.load_state_dict(torch.load('agente_dqn_mujoco.pt', map_location=torch.device('cpu')))
    iteraciones = 0
    recompensa = 0
    lista_recompensas = []
    while(iteraciones < 5):
        action = epsilon_greedy(observation, 0.0, env, modelo)
        act_cont = d2c(action)
        observation, reward, done, truncated, info = env.step(act_cont)
        recompensa += reward
    
        if done or truncated:
            observation, info = env.reset()
            iteraciones += 1
            lista_recompensas.append(recompensa)
            recompensa = 0
    print("Recompensas", lista_recompensas)
    
main()

