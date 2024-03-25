
import gymnasium as gym
import random
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torch

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
        
def epsilon_greedy(state, epsilon, env, main_nn):
    result = np.random.uniform()
    if result < epsilon:
        return env.action_space.sample() # acción aleatoria
    else:
        qs = main_nn(torch.from_numpy(state)).cpu().data.numpy()
        return np.argmax(qs) # acción greedy

def main():
    modelo = DQN(4, 2)
    modelo.load_state_dict(torch.load('agente_dqn.pt'))
    env = gym.make('CartPole-v1', render_mode='human')
    observation, info = env.reset()
    recompensa_pe = 0
    recompensa_lista = []
    iteraciones = 0
    while(iteraciones < 10):
        action = epsilon_greedy(observation, 0.01, env, modelo)
        observation, reward, terminated, truncated, info = env.step(action)
        recompensa_pe += reward
    
        if terminated or truncated:
            observation, info = env.reset()
            iteraciones += 1
            recompensa_lista.append(recompensa_pe)
            recompensa_pe = 0
    print("Recompensa final:", recompensa_lista)
    env.close()

main()


