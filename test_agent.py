from stable_baselines3 import DQN
from maze_env import MazeEnv
import time
import numpy as np

def test_trained_agent(model_path="models/best_model.zip"):
    """Тестирование обученного агента"""
    
    # Загружаем обученную модель
    try:
        model = DQN.load(model_path)
        print(f"Модель загружена из {model_path}")
    except FileNotFoundError:
        print(f"Модель не найдена в {model_path}")
        print("Сначала запустите обучение: python train_agent.py")
        return
    
    # Создаем среду
    env = MazeEnv()
    
    # Тестируем агента
    print("\nТестирование обученного агента...")
    
    for episode in range(5):  # Тестируем 5 эпизодов
        obs, info = env.reset()
        total_reward = 0
        steps = 0
        max_steps = 100  # Максимум 100 шагов на эпизод
        
        print(f"\nЭпизод {episode + 1}:")
        
        while steps < max_steps:
            # Агент выбирает действие
            action, _ = model.predict(obs, deterministic=True)
            
            # Выполняем действие
            obs, reward, done, truncated, info = env.step(action)
            
            total_reward += reward
            steps += 1
            
            # Отрисовываем
            env.render()
            time.sleep(0.1)  # Замедляем для визуализации
            
            # Выводим информацию о шаге
            action_names = ["Вверх", "Вправо", "Вниз", "Влево"]
            print(f"  Шаг {steps}: Действие={action_names[action]}, "
                  f"Позиция={obs}, Награда={reward:.1f}")
            
            if done:
                if obs[0] == 9 and obs[1] == 9:
                    print(f"  ✅ УСПЕХ! Достигнут финиш за {steps} шагов")
                else:
                    print(f"  ❌ Эпизод завершен за {steps} шагов")
                break
        
        print(f"  Итоговая награда: {total_reward:.1f}")
        
        if steps >= max_steps:
            print(f"  ⚠️ Превышен лимит шагов ({max_steps})")
    
    env.close()
    print("\nТестирование завершено!")

def show_agent_stats(model_path="models/best_model.zip"):
    """Показывает статистику обученного агента"""
    
    try:
        model = DQN.load(model_path)
        print(f"Статистика модели из {model_path}:")
        print(f"- Тип политики: {model.policy}")
        print(f"- Размер сети: {model.policy.net_arch}")
        print(f"- Параметры: {sum(p.numel() for p in model.policy.parameters())} параметров")
    except FileNotFoundError:
        print("Модель не найдена")

if __name__ == "__main__":
    show_agent_stats()
    test_trained_agent() 