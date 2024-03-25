
import gymnasium as gym
import random
import csv

#from gymnasium.envs.toy_text.frozen_lake import generate_random_map

## Juega 10 veces dada una política
def partida(politica):
    env = gym.make('FrozenLake-v1', desc=["SFFF", "FFFF", "FFFF", "FFFG"], map_name="4x4", is_slippery=True, render_mode="human")
    env.reset()

    iteraciones = 0
    recompensa = 0
    observation = 0
    while(iteraciones < 10):
        action = politica[observation]
        observation, reward, terminated, truncated, info = env.step(action)
        recompensa += reward
        if terminated or truncated:
            observation, info = env.reset()
            iteraciones += 1
    env.close()
    return recompensa

def main():
    # Para este punto ya deberían existir los archivos en CSV
    print("Elija una política:\n1. Por iteración de política.\n2. Por iteración de valor.")
    opcion = input()
    if opcion == "1":
        archivo = open("politicaIP.csv")
    else:
        archivo = open("politicaIV.csv")
    politica = []
    csv_reader = csv.reader(archivo, delimiter=",")
    for row in csv_reader:
        politica.append(int(row[1]))
    rt = partida(politica)
    print("Recompensa total:", rt)

main()