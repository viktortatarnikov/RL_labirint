# Лабиринт с Reinforcement Learning

Этот проект демонстрирует применение reinforcement learning для решения лабиринта с использованием Gymnasium и Stable Baselines3. Проект включает как оригинальную игру на pygame, так и среду для обучения ИИ-агентов.

## Структура проекта

### Основные файлы
- `Main_labirint.py` - игра лабиринт на pygame (управление стрелками)
- `maze_env.py` - среда Gymnasium для reinforcement learning
- `requirements.txt` - зависимости проекта

### Файлы для обучения агентов
- `train_agent.py` - **ОСНОВНОЙ файл обучения DQN агента** (требует доработки)
- `simple_train_agent.py` - упрощенное обучение PPO агента
- `test_agent.py` - тестирование обученного агента
- `test_env.py` - тестирование среды

### Файлы визуализации
- `agent_training_visualize.py` - визуализация обученного DQN агента
- `simple_agent_vizualaiser.py` - визуализация обученного PPO агента

### Модели и данные
- `models/` - папка для сохранения обученных моделей
- `ppo_maze_agent.zip` - предобученная PPO модель
- `ppo-maze-10_000.zip` - предобученная PPO модель (10k шагов)

##  Быстрый старт

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Игра в оригинальный лабиринт
```bash
python Main_labirint.py
```
**Управление**: стрелки клавиатуры

### 3. Тестирование среды
```bash
python test_env.py
```

### 4. Обучение агента (выберите один из вариантов)

#### Вариант A: Простое обучение PPO (рекомендуется)
```bash
python simple_train_agent.py
```

#### Вариант B: Полное обучение DQN (требует доработки)
```bash
python train_agent.py
```

### 5. Визуализация результатов

#### Для PPO агента:
```bash
python simple_agent_vizualaiser.py
```

#### Для DQN агента:
```bash
python agent_training_visualize.py
```

### 6. Тестирование агента
```bash
python test_agent.py
```

##  Известные проблемы

### Проблемы с `train_agent.py`
Основной файл обучения `train_agent.py` имеет следующие проблемы:

1. **Нестабильное обучение**: DQN агент может не сходиться к оптимальному решению
2. **Проблемы с гиперпараметрами**: текущие настройки могут быть неоптимальными для данной среды
3. **Отсутствие валидации**: нет проверки качества обучения в процессе
4. **Проблемы с сохранением**: модель может не сохраняться корректно

### Рекомендации по исправлению
- Использовать `simple_train_agent.py` как основу для обучения
- Экспериментировать с гиперпараметрами (learning_rate, buffer_size, etc.)
- Добавить больше эпох обучения (увеличить `total_timesteps`)
- Реализовать callback для мониторинга прогресса

##  Как работает Reinforcement Learning

### Среда (Environment)
- **Состояние**: позиция агента в лабиринте (x, y координаты)
- **Действия**: 4 направления движения (0-вверх, 1-вправо, 2-вниз, 3-влево)
- **Награды**: 
  - `+100` за достижение финиша
  - `-1` за столкновение со стеной
  - `-0.1` за каждый ход (штраф за время)

### Алгоритмы
- **DQN** (Deep Q-Network) - для дискретных действий
- **PPO** (Proximal Policy Optimization) - более стабильный алгоритм

### Лабиринт
```
S - старт (0,0), F - финиш (9,9)
S . # . . . . . . .
. . # . # # # # . .
. . # . # . . # . .
. . # . # . # # . .
. . . . . . # . . .
. # # # . # # # # .
. # . # . . . . # .
. # . # # # # . # .
. . . . . . . . # .
# # # # # # # # # F
```

##  Результаты

### PPO агент (10,000 шагов)
- Успешно находит путь к финишу
- Среднее время: ~20-30 шагов
- Стабильное обучение

### DQN агент (10,000 шагов)
- Требует больше времени для сходимости
- Менее стабильные результаты
- Нуждается в настройке гиперпараметров

## 🔧 Технические детали

### Зависимости
- `gymnasium==0.29.1` - среда для RL
- `stable-baselines3==2.1.0` - алгоритмы RL
- `torch==2.1.0` - PyTorch для нейронных сетей
- `pygame==2.5.2` - визуализация
- `numpy==1.24.3` - численные вычисления
- `matplotlib==3.7.2` - графики

### Структура среды
- Размер лабиринта: 10x10
- Размер ячейки: 50x50 пикселей
- Окно: 500x500 пикселей

## 🎯 Следующие шаги

1. **Исправить `train_agent.py`**:
   - Оптимизировать гиперпараметры
   - Добавить валидацию обучения
   - Улучшить систему сохранения моделей

2. **Добавить новые функции**:
   - Генерация случайных лабиринтов
   - Сравнение алгоритмов
   - Визуализация процесса обучения

3. **Улучшить визуализацию**:
   - Графики обучения
   - Статистика успешности
   - Интерактивная демонстрация


## Лицензия

Этот проект предназначен для образовательных целей. 

---

# Maze with Reinforcement Learning (English)

This project demonstrates the use of reinforcement learning to solve a maze using Gymnasium and Stable Baselines3. The project includes both the original maze game on pygame and an environment for training AI agents.

## Project Structure

### Main files
- `Main_labirint.py` - the original maze game on pygame (arrow key controls)
- `maze_env.py` - Gymnasium environment for reinforcement learning
- `requirements.txt` - project dependencies

### Agent training files
- `train_agent.py` - **MAIN DQN agent training script** (**needs improvement, see below**)
- `simple_train_agent.py` - simplified PPO agent training
- `test_agent.py` - test a trained agent
- `test_env.py` - test the environment

### Visualization files
- `agent_training_visualize.py` - visualize a trained DQN agent
- `simple_agent_vizualaiser.py` - visualize a trained PPO agent

### Models and data
- `models/` - directory for saved models
- `ppo_maze_agent.zip` - pretrained PPO model
- `ppo-maze-10_000.zip` - pretrained PPO model (10k steps)

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Play the original maze game
```bash
python Main_labirint.py
```
**Controls**: arrow keys

### 3. Test the environment
```bash
python test_env.py
```

### 4. Train an agent (choose one)

#### Option A: Simple PPO training (recommended)
```bash
python simple_train_agent.py
```

#### Option B: Full DQN training (**needs improvement**)
```bash
python train_agent.py
```

### 5. Visualize results

#### For PPO agent:
```bash
python simple_agent_vizualaiser.py
```

#### For DQN agent:
```bash
python agent_training_visualize.py
```

### 6. Test a trained agent
```bash
python test_agent.py
```

## Known Issues

### Problems with `train_agent.py`
The main training script `train_agent.py` has the following issues:

1. **Unstable training**: DQN agent may not converge to an optimal solution
2. **Hyperparameter issues**: current settings may be suboptimal for this environment
3. **No validation**: no quality check during training
4. **Saving issues**: model may not save correctly

### Recommendations
- Use `simple_train_agent.py` as a base for training
- Experiment with hyperparameters (learning_rate, buffer_size, etc.)
- Increase the number of training steps (`total_timesteps`)
- Add callbacks for monitoring progress

## How Reinforcement Learning Works

### Environment
- **State**: agent's position in the maze (x, y coordinates)
- **Actions**: 4 movement directions (0-up, 1-right, 2-down, 3-left)
- **Rewards**:
  - `+100` for reaching the finish
  - `-1` for hitting a wall
  - `-0.1` for each step (time penalty)

### Algorithms
- **DQN** (Deep Q-Network) - for discrete actions
- **PPO** (Proximal Policy Optimization) - more stable for this task

### Maze layout
```
S - start (0,0), F - finish (9,9)
S . # . . . . . . .
. . # . # # # # . .
. . # . # . . # . .
. . # . # . # # . .
. . . . . . # . . .
. # # # . # # # # .
. # . # . . . . # .
. # . # # # # . # .
. . . . . . . . # .
# # # # # # # # # F
```

## Results

### PPO agent (10,000 steps)
- Successfully finds a path to the finish
- Average time: ~20-30 steps
- Stable training

### DQN agent (10,000 steps)
- Needs more time to converge
- Less stable results
- Requires hyperparameter tuning

## Technical Details

### Dependencies
- `gymnasium==0.29.1` - RL environment
- `stable-baselines3==2.1.0` - RL algorithms
- `torch==2.1.0` - PyTorch for neural networks
- `pygame==2.5.2` - visualization
- `numpy==1.24.3` - numerical computations
- `matplotlib==3.7.2` - plots

### Environment structure
- Maze size: 10x10
- Cell size: 50x50 pixels
- Window: 500x500 pixels

## Next Steps

1. **Fix `train_agent.py`**:
   - Optimize hyperparameters
   - Add training validation
   - Improve model saving

2. **Add new features**:
   - Random maze generation
   - Algorithm comparison
   - Training process visualization

3. **Improve visualization**:
   - Training graphs
   - Success statistics
   - Interactive demo

## License

This project is for educational purposes only. 