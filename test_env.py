from maze_env import MazeEnv
import time

def test_maze_env():
    """Тестирование среды лабиринта"""
    
    # Создаем среду
    env = MazeEnv()
    
    print("Тестирование среды лабиринта...")
    print(f"Размер действия: {env.action_space}")
    print(f"Размер наблюдения: {env.observation_space}")
    
    # Сбрасываем среду
    obs, info = env.reset()
    print(f"Начальное состояние: {obs}")
    
    # Тестируем несколько случайных действий
    for i in range(10):
        # Случайное действие
        action = env.action_space.sample()
        print(f"Действие {i+1}: {action}")
        
        # Выполняем действие
        obs, reward, done, truncated, info = env.step(action)
        print(f"  Новое состояние: {obs}")
        print(f"  Награда: {reward}")
        print(f"  Завершено: {done}")
        
        # Отрисовываем
        env.render()
        time.sleep(0.5)  # Пауза для визуализации
        
        if done:
            print("Достигнут финиш!")
            break
    
    env.close()
    print("Тест завершен!")

if __name__ == "__main__":
    test_maze_env() 