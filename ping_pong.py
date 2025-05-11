# from pygame import *
# from random import randint


# # font.init()
# # font = font.Font(None, 36)
# # win = font.render('I PLAYER WIN!', True, (50, 150, 50))
# # win1 = font.render('II PLAYER WIN!', True, (180, 0, 0))

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def draw(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))


# # Класс игроков (ракетки), наследуется от GameSprite
# class Player(GameSprite):
#     # Обновление позиции правой ракетки (управляется стрелочками вверх-вниз)
#     def update_r(self):
#         keys = key.get_pressed()  # Проверяем нажатия клавиш
#         if keys[K_UP] and self.rect.y > 5:  # Если нажата клавиша вверх и верхняя граница поля не достигнута
#             self.rect.y -= self.speed  # Ракетка движется вверх
#         if keys[K_DOWN] and self.rect.y < 620:  # Если нажата клавиша вниз и нижняя граница поля не достигнута
#             self.rect.y += self.speed  # Ракетка движется вниз


#     # Обновление позиции левой ракетки (управляется WASD)
#     def update_l(self):
#         keys = key.get_pressed()  # Проверяем нажатия клавиш
#         if keys[K_w] and self.rect.y > 5:  # Если нажата клавиша W и верхняя граница поля не достигнута
#             self.rect.y -= self.speed  # Ракетка движется вверх
#         if keys[K_s] and self.rect.y < win_height - 80:  # Если нажата клавиша S и нижняя граница поля не достигнута
#             self.rect.y += self.speed  # Ракетка движется вниз


# win_width = 700
# win_height = 500
# red = (255, 160, 122)
# window = display.set_mode((win_width, win_height))
# # clock = pygame.time.Clock()
# window.fill(red)
# display.set_caption('ping pong')


# ship = Player('platform.png', 30, 200, 50, 150, 7)
# ship2 = Player('platform.png', 620, 200, 50, 150, 7)
# ball = GameSprite('ball.png', 200, 200, 50, 50, 50)


# clock = time.Clock()
# FPS = 60


from pygame import *  # Импортируем библиотеку Pygame для разработки графического приложения


'''Необходимые классы'''




# Класс-родитель для всех игровых объектов-спрайтов
class GameSprite(sprite.Sprite):
    # Конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()  # Наследуем родительские методы Sprite
        self.image = transform.scale(image.load(player_image), (width, height))  # Загружаем картинку персонажа и масштабируем её
        self.speed = player_speed  # Скорость передвижения спрайта
        self.rect = self.image.get_rect()  # Получаем прямоугольник для позиционирования спрайта
        self.rect.x = player_x  # Начальная позиция X
        self.rect.y = player_y  # Начальная позиция Y


    # Метод для отображения спрайта на экране
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))  # Рисование изображения на окне в заданных координатах




# Класс игроков (ракетки), наследуется от GameSprite
class Player(GameSprite):
    # Обновление позиции правой ракетки (управляется стрелочками вверх-вниз)
    def update_r(self):
        keys = key.get_pressed()  # Проверяем нажатия клавиш
        if keys[K_UP] and self.rect.y > 5:  # Если нажата клавиша вверх и верхняя граница поля не достигнута
            self.rect.y -= self.speed  # Ракетка движется вверх
        if keys[K_DOWN] and self.rect.y < win_height - 80:  # Если нажата клавиша вниз и нижняя граница поля не достигнута
            self.rect.y += self.speed  # Ракетка движется вниз


    # Обновление позиции левой ракетки (управляется WASD)
    def update_l(self):
        keys = key.get_pressed()  # Проверяем нажатия клавиш
        if keys[K_w] and self.rect.y > 5:  # Если нажата клавиша W и верхняя граница поля не достигнута
            self.rect.y -= self.speed  # Ракетка движется вверх
        if keys[K_s] and self.rect.y < win_height - 80:  # Если нажата клавиша S и нижняя граница поля не достигнута
            self.rect.y += self.speed  # Ракетка движется вниз




# Игровое окно и фон
back = (200, 255, 255)  # Цвет фона окна (светло-голубой)
win_width = 600  # Ширина игрового окна
win_height = 500  # Высота игрового окна
window = display.set_mode((win_width, win_height))  # Создаем окно с указанными размерами
window.fill(back)  # Заливаем экран цветом фона




# Флаги состояния игры
game = True  # Игра запущена?
finish = False  # Игра закончена?
clock = time.Clock()  # Таймер для управления частотой кадров
FPS = 60  # Частота обновления кадра (frames per second)




# Создание игровых объектов
racket1 = Player('platform.png', 30, 200, 4, 50, 150)  # Левая ракетка слева
racket2 = Player('platform.png', 520, 200, 4, 50, 150)  # Правая ракетка справа
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)  # Мяч в центре экрана




# Шрифты и надписи
font.init()  # Инициализация шрифтового модуля
font = font.Font(None, 35)  # Основной шрифт
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))  # Надпись проигрыша игрока 1
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))  # Надпись проигрыша игрока 2




# Направления скорости мяча
speed_x = 3  # Горизонтальное движение
speed_y = 3  # Вертикальное движение




# Главный цикл игры
while game:
    for e in event.get():  # Обработка событий
        if e.type == QUIT:  # Если событие выхода
            game = False  # Завершаем игру


    if not finish:  # Пока игра продолжается
        window.fill(back)  # Очищаем экран перед обновлением
        racket1.update_l()  # Обновляем позицию левой ракетки
        racket2.update_r()  # Обновляем позицию правой ракетки
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1, (200, 200))
            game_over = True 
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True


        # Рисуем объекты на экране
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()  # Обновляем экран
    clock.tick(FPS)  # Ограничиваем частоту кадров


