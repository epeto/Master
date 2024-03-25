
import gymnasium as gym
import random
import numpy

env = gym.make('InvertedPendulum-v4', render_mode='human')
env.reset()

iteraciones = 0
recompensa = 0
while(iteraciones < 10):
    action = random.random()*6 - 3
    observation, reward, terminated, truncated, info = env.step((action,))
    print(observation)
    recompensa += reward
    
    if terminated or truncated:
        observation, info = env.reset()
        iteraciones += 1
print("Recompensa final:", reward)

env.close()

