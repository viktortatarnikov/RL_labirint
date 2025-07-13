import pygame
import sys

# инициализация pygame
pygame.init()

# Задание размеров окна и цветов
width, height = 500, 500
cell_size = width // 10

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# создаём окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Лабиринт')

# Определение лабиринта
maze = [
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
]

# начальная позиция робота
robot_pos = [0, 0]
# конечная позиция
finish_pos = [9, 9]

# функция для рисования сетки
def draw_grid():
    for x in range(10):
        for y in range(10):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if maze[y][x] == 1:
                pygame.draw.rect(screen, black, rect)
            else:
                pygame.draw.rect(screen, white, rect)
                pygame.draw.rect(screen, white, rect, 1)

# функция для рисования робота
def draw_robot():
    x, y = robot_pos
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, blue, rect)

# функция для рисования финиша
def draw_finish():
    x, y = finish_pos
    rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen,green, rect)

# функция для отображения сообщения об успехе
def show_success_messege():
    font = pygame.font.SysFont(None, 55)
    text = font.render('Успех! Играть снова?', True, green)
    text_rect = text.get_rect(center=(width // 2, height // 2))

    # рисуем белый прямоугольник под текстом
    beckground_rect = pygame.Rect(
        text_rect.left - 20,
        text_rect.top - 20,
        text_rect.width + 40,
        text_rect.height + 40
    )
    pygame.draw.rect(screen, white, beckground_rect)

    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # начать занова при нажатии enter
                    return True
                elif event.key == pygame.K_ESCAPE: # Выйти из игры при нажатии esc
                    pygame.quit()
                    sys.exit()

# основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and robot_pos[0] > 0 and maze[robot_pos[1]][robot_pos[0] - 1] == 0:
                robot_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and robot_pos[0] < 9 and maze[robot_pos[1]][robot_pos[0] + 1] == 0:
                robot_pos[0] += 1
            elif event.key == pygame.K_UP and robot_pos[1] > 0 and maze[robot_pos[1] - 1][robot_pos[0]] == 0:
                robot_pos[1] -= 1
            elif event.key == pygame.K_DOWN and robot_pos[1] < 9 and maze[robot_pos[1] + 1][robot_pos[0]] == 0:
                robot_pos[1] += 1

    screen.fill(black)
    draw_grid()
    draw_robot()
    draw_finish()
    pygame.display.flip()

    # проверка на достижение финиша
    if robot_pos == finish_pos:
        if show_success_messege():
            # сброс начальной позиции робота для нового начала
            robot_pos = [0, 0]

pygame.quit()
sys.exit()