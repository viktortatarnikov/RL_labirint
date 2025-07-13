from stable_baselines3 import DQN
from maze_env import MazeEnv
import pygame
import time

def visualize_trained_agent(model_path="models/best_model.zip"):
    """Визуализация обученного агента"""
    
    # Загружаем обученную модель
    try:
        model = DQN.load(model_path)
        print(f"Модель загружена из {model_path}")
    except FileNotFoundError:
        print(f"Модель не найдена в {model_path}")
        print("Сначала запустите обучение: python train_agent.py")
        return
    except Exception as e:
        print(f"Ошибка загрузки модели: {e}")
        return
    
    # Создаем среду
    env = MazeEnv()
    
    # Сбрасываем среду
    obs, _ = env.reset()
    done = False
    steps = 0
    max_steps = 200  # Максимум 200 шагов
    
    print("Начинаем визуализацию агента...")
    print("Нажмите любую клавишу для продолжения или ESC для выхода")
    
    while not done and steps < max_steps:
        # Агент выбирает действие
        action, _ = model.predict(obs, deterministic=True)
        
        # Выполняем действие
        obs, reward, done, truncated, info = env.step(action)
        
        steps += 1
        
        # Отрисовываем
        env.render()
        
        # Обработка событий pygame
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print("Визуализация прервана пользователем")
                    env.close()
                    return
        
        # Замедляем для лучшей визуализации
        pygame.time.wait(200)
        
        # Выводим информацию о шаге
        action_names = ["Вверх", "Вправо", "Вниз", "Влево"]
        print(f"Шаг {steps}: Действие={action_names[action]}, "
              f"Позиция=({obs[0]}, {obs[1]}), Награда={reward:.1f}")
        
        if done:
            if obs[0] == 9 and obs[1] == 9:
                print(f"✅ УСПЕХ! Достигнут финиш за {steps} шагов")
            else:
                print(f"❌ Эпизод завершен за {steps} шагов")
            break
    
    if steps >= max_steps:
        print(f"⚠️ Превышен лимит шагов ({max_steps})")
    
    env.close()
    print("Визуализация завершена!")

if __name__ == "__main__":
    visualize_trained_agent()