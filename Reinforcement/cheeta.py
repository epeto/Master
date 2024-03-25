
import gymnasium as gym
import random
import numpy

env = gym.make('HalfCheetah-v4', render_mode='human')
env.reset()

iteraciones = 0
recompensa = 0
while(iteraciones < 1):
    action = numpy.random.randn(6)
    observation, reward, terminated, truncated, info = env.step(action)
    print(observation)
    recompensa += reward
    
    if terminated or truncated:
        observation, info = env.reset()
        iteraciones += 1
print("Recompensa final:", reward)

env.close()
