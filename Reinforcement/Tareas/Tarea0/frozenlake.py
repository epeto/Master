
import gymnasium as gym
import random

from gymnasium.envs.toy_text.frozen_lake import generate_random_map

env = gym.make('FrozenLake-v1', desc=generate_random_map(size=4), map_name="4x4", is_slippery=True, render_mode="human")
env.reset()

iteraciones = 0
recompensa = 0
while(iteraciones < 10):
    action = random.randint(0, 3)
    observation, reward, terminated, truncated, info = env.step(1)
    recompensa += reward
    
    if terminated or truncated:
        observation, info = env.reset()
        iteraciones += 1
print('Espacio de observación:', env.observation_space.shape)
print("Recompensa final:", reward)

env.close()

