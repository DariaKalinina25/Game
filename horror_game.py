import pygame  # Импортируем библиотеку Pygame
import sys     # Импортируем sys для выхода из игры

# Инициализация Pygame
pygame.init()

# Параметры окна
width, height = 800, 500  # Ширина и высота окна
screen = pygame.display.set_mode((width, height))  # Создаем окно с указанными параметрами
pygame.display.set_caption("Person Game - Урок 1")  # Устанавливаем заголовок окна

# Загрузка статичного фона
static_background_image = pygame.image.load('голубой_фон.jpg')  # Загружаем изображение фона
static_background_image = pygame.transform.scale(static_background_image, (width, height))  # Масштабируем его под размер окна

# Загрузка изображения персонажа
person_image = pygame.image.load('шар.png')  # Загружаем изображение персонажа
person_image = pygame.transform.scale(person_image, (50, 50))  # Масштабируем изображение

# Позиция персонажа
person_x = 50  # Начальная позиция персонажа по X
person_y = height - person_image.get_height() - 10  # Начальная позиция персонажа по Y

# Основной игровой цикл
def game_loop():
    running = True  # Флаг для управления циклом
    while running:
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:  # Если закрыть окно
                pygame.quit()
                sys.exit()
        
        # Отображение фона
        screen.blit(static_background_image, (0, 0))  # Отображаем фон
        
        # Отображение персонажа
        screen.blit(person_image, (person_x, person_y))  # Отображаем персонажа на экране
        
        # Обновляем экран
        pygame.display.flip()  # Обновляем экран
        
        # Ограничение FPS
        pygame.time.Clock().tick(60)  # Устанавливаем частоту обновления экрана в 60 кадров в секунду

# Запуск игры
game_loop()  # Запускаем основной игровой цикл
