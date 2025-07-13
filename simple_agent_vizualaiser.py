from stable_baselines3 import PPO
from maze_env import MazeEnv
import pygame

env = MazeEnv()
model = PPO.load("ppo-maze-10_000")

obs, _ = env.reset()
done = False

while not done:
    action, _ = model.predict(obs, deterministic=True)
    print(action)
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    pygame.time.wait(100)

env.close()