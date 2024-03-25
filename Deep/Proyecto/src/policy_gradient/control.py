
import argparse
import gymnasium as gym
import torch.nn as nn
import torch
import numpy as np


class Actor(nn.Module):
    def __init__(self, obs_size, act_size):
        super(Actor, self).__init__()

        self.net = nn.Sequential(
            #nn.BatchNorm1d(obs_size),
            nn.Linear(obs_size, 400),
            nn.ReLU(),
            nn.Linear(400, 300),
            nn.ReLU(),
            nn.Linear(300, act_size),
            nn.Tanh())

    def forward(self, x):
        # en el caso de cartpole de Mujoco, la señal está en el rango [-3,3]
        # por eso se multiplica el resultado de tanh por 3
        return 3*self.net(x)
        
        
def main():
    env = gym.make('InvertedPendulum-v4', render_mode='human')
    observation, info = env.reset()
    modelo = Actor(env.observation_space.shape[0], env.action_space.shape[0])
    modelo.load_state_dict(torch.load('actor_params.pt', map_location=torch.device('cpu')))
    iteraciones = 0
    recompensa = 0
    lista_recompensas = []
    while(iteraciones < 5):
        mu = modelo(torch.tensor(observation, dtype=torch.float32))
        #print(mu)
        action = mu.squeeze(dim=0).detach().numpy()
        #print(action)
        action = np.clip(action, -3, 3)
        #print(action)
        observation, reward, done, truncated, info = env.step((action,))
        recompensa += reward
    
        if done or truncated:
            observation, info = env.reset()
            iteraciones += 1
            lista_recompensas.append(recompensa)
            recompensa = 0
    print("Recompensas", lista_recompensas)
    
main()
