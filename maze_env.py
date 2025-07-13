import gymnasium as gym
import numpy as np
import pygame
from gymnasium import spaces

class MazeEnv(gym.Env):
    """
    Среда лабиринта для reinforcement learning
    """
    
    def __init__(self):
        super().__init__()
        
        # Размеры лабиринта
        self.maze_size = 10
        self.cell_size = 50
        self.width = self.height = self.maze_size * self.cell_size
        
        # Определение лабиринта (0 - проход, 1 - стена)
        self.maze = np.array([
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ])
        
        # Начальная и конечная позиции
        self.start_pos = [0, 0]
        self.finish_pos = [9, 9]
        
        # Позиция агента
        self.agent_pos = None
        
        # Определяем пространства
        # Действия: 0-вверх, 1-вправо, 2-вниз, 3-влево
        self.action_space = spaces.Discrete(4)
        
        # Состояние: позиция агента (x, y)
        self.observation_space = spaces.Box(
            low=0, high=self.maze_size-1, shape=(2,), dtype=np.int32
        )
        
        # Инициализация pygame для рендеринга
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Maze RL Environment')
        
        # Цвета
        self.colors = {
            'white': (255, 255, 255),
            'black': (0, 0, 0),
            'blue': (0, 0, 255),
            'green': (0, 255, 0),
            'red': (255, 0, 0)
        }
    
    def reset(self, seed=None):
        """Сброс среды к начальному состоянию"""
        super().reset(seed=seed)
        
        # Устанавливаем агента в начальную позицию
        self.agent_pos = self.start_pos.copy()
        
        return np.array(self.agent_pos, dtype=np.int32), {}
    
    def step(self, action):
        """Выполнение действия и получение награды"""
        # Сохраняем старую позицию
        old_pos = self.agent_pos.copy()
        
        # Выполняем действие
        if action == 0:  # Вверх
            new_pos = [self.agent_pos[0], max(0, self.agent_pos[1] - 1)]
        elif action == 1:  # Вправо
            new_pos = [min(self.maze_size - 1, self.agent_pos[0] + 1), self.agent_pos[1]]
        elif action == 2:  # Вниз
            new_pos = [self.agent_pos[0], min(self.maze_size - 1, self.agent_pos[1] + 1)]
        elif action == 3:  # Влево
            new_pos = [max(0, self.agent_pos[0] - 1), self.agent_pos[1]]
        
        # Проверяем, можно ли двигаться в новую позицию
        if self.maze[new_pos[1]][new_pos[0]] == 0:
            self.agent_pos = new_pos
        
        # Определяем награду
        reward = -0.1  # Небольшой штраф за каждый ход
        
        # Достигли финиша
        done = False
        if self.agent_pos == self.finish_pos:
            reward = 100.0  # Большая награда за достижение цели
            done = True
        
        # Столкновение со стеной
        elif self.agent_pos == old_pos and action in [0, 1, 2, 3]:
            reward = -1.0  # Штраф за столкновение
        
        return np.array(self.agent_pos, dtype=np.int32), reward, done, False, {}
    
    def render(self):
        """Отрисовка среды"""
        self.screen.fill(self.colors['black'])
        
        # Рисуем лабиринт
        for x in range(self.maze_size):
            for y in range(self.maze_size):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, 
                                 self.cell_size, self.cell_size)
                if self.maze[y][x] == 1:
                    pygame.draw.rect(self.screen, self.colors['black'], rect)
                else:
                    pygame.draw.rect(self.screen, self.colors['white'], rect)
                    pygame.draw.rect(self.screen, self.colors['white'], rect, 1)
        
        # Рисуем агента
        agent_rect = pygame.Rect(self.agent_pos[0] * self.cell_size, 
                               self.agent_pos[1] * self.cell_size, 
                               self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.colors['blue'], agent_rect)
        
        # Рисуем финиш
        finish_rect = pygame.Rect(self.finish_pos[0] * self.cell_size, 
                                self.finish_pos[1] * self.cell_size, 
                                self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, self.colors['green'], finish_rect)
        
        pygame.display.flip()
    
    def close(self):
        """Закрытие среды"""
        pygame.quit() 