from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import EvalCallback
from maze_env import MazeEnv
import torch
import os
# import tqdm
# import rich

# Создаем папку models если её нет
os.makedirs("models", exist_ok=True)

# Создаем среду с мониторингом
env = MazeEnv()
env = Monitor(env)

# Проверяем среду
check_env(env, warn=True)

# Создаем среду для оценки
eval_env = MazeEnv()
eval_env = Monitor(eval_env)

# Создаем callback для оценки
eval_callback = EvalCallback(
    eval_env,
    best_model_save_path="models/",
    log_path="models/",
    eval_freq=1000,
    deterministic=True,
    render=False
)

# Создаем модель DQN
model = DQN(
    "MlpPolicy", 
    env, 
    device="cuda" if torch.cuda.is_available() else "cpu", 
    verbose=1,
    learning_rate=0.0001,
    buffer_size=10000,
    learning_starts=1000,
    batch_size=32,
    gamma=0.99,
    train_freq=4,
    gradient_steps=1,
    target_update_interval=1000,
    exploration_fraction=0.1,
    exploration_initial_eps=1.0,
    exploration_final_eps=0.05
)

print("Начинаем обучение агента...")
print(f"Используется устройство: {'CUDA' if torch.cuda.is_available() else 'CPU'}")

# Обучаем модель
model.learn(
    total_timesteps=10000,
    callback=eval_callback,
    # progress_bar=True
)

# Сохраняем финальную модель
model.save("models/final_model")
print("Обучение завершено! Модель сохранена в models/final_model")
print("Лучшая модель сохранена в models/best_model")

