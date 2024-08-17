import pygame  # Импорт библиотеки Pygame для работы с графикой и вводом
import sys     # Импорт модуля sys для работы с системными функциями

# Инициализация Pygame
pygame.init()

# Параметры окна
width, height = 800, 500  # Ширина и высота окна
screen = pygame.display.set_mode((width, height))  # Создание окна с указанными параметрами
pygame.display.set_caption("Horror game")  # Установка заголовка окна

# Загрузка изображения персонажа
person_image = pygame.image.load('person.png')  # Загрузка изображения персонажа
person_image = pygame.transform.scale(person_image, (50, 50))  # Масштабирование изображения под нужный размер

# Начальные координаты персонажа
person_x = 50  # Позиция по X
person_y = height - person_image.get_height() - 10  # Позиция по Y

# Основной игровой цикл
def game_loop():
    running = True  # Флаг для управления циклом
    clock = pygame.time.Clock()  # Создание объекта Clock для управления FPS

    while running:
        for event in pygame.event.get():  # Обработка всех событий
            if event.type == pygame.QUIT:  # Если закрыть окно
                pygame.quit()
                sys.exit()

        # Отображение белого фона
        screen.fill((255, 255, 255))  # Заполнение экрана белым цветом
        
        # Отображение персонажа
        screen.blit(person_image, (person_x, person_y))  # Рисуем персонажа на экране

        # Обновление экрана
        pygame.display.flip()  # Обновление экрана

        # Ограничение FPS
        clock.tick(60)  # Установка частоты обновления экрана в 60 кадров в секунду

# Запуск игры
game_loop()  # Запуск основного игрового цикла
