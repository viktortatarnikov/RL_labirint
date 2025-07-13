from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from maze_env import MazeEnv

env = MazeEnv()

# Проверка среды на совместимость
check_env(env, warn=True)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

model.save("ppo-maze-10_000")