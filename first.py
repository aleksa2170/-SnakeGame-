import pygame
import random

pygame.init()

# задаём цвета
Y = (255, 255, 102)
B = (0, 0, 0)
R = (213, 50, 80)
G = (0, 255, 0)

# ширина и длина поля
playing_field_width = 900
playing_field_height = 600

# создание поля
playing_field = pygame.display.set_mode((playing_field_width, playing_field_height))
pygame.display.set_caption('Snake Game')

# добавим игре время
clock = pygame.time.Clock()

# создание змейки
SNAKE_BLOCK = 10
SNAKE_SPEED = 10

# создание надписи счет
font_style = pygame.font.SysFont("bold", 25)
font_check = pygame.font.SysFont("comicsansms", 35)


# выводим "счет" на экран
def check(sc):
    value = font_check.render("Счет: " + str(sc), True, R)
    playing_field.blit(value, [0, 0])


# выводим змейку на экран
def snake(SNAKE_block, SNAKE_List):
    for x in SNAKE_List:
        pygame.draw.rect(playing_field, G, [x[0], x[1], SNAKE_block, SNAKE_block])


# сообщение о проигрыше
def sms(smsg, color):
    mesg = font_style.render(smsg, True, color)
    playing_field.blit(mesg, [playing_field_width / 6, playing_field_height / 3])


# создаем цикл игры
def gameLoop():
    game_OVER = False
    game_CLOSE = False

    x1 = playing_field_width / 2
    y1 = playing_field_height / 2

    x1_change = 0
    y1_change = 0

    SNAKE_List = []
    Long_SNAKE = 1

    # делаем так чтобы игра появлялась в рандомном месте
    foodx = round(random.randrange(0, playing_field_width - SNAKE_BLOCK) / 10.0) * 10.0
    foody = round(random.randrange(0, playing_field_height - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_OVER:

        # добавляем вывод смс о проигрыше
        while game_CLOSE:
            playing_field.fill(B)
            sms("Ты проиграл! Нажми A - Again, чтобы сыграть заново или Q - Quit, чтобы выйти", R)
            check(Long_SNAKE - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_OVER = True
                        game_CLOSE = False
                    if event.key == pygame.K_a:
                        gameLoop()

        # добавляем движение змейке
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_OVER = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= playing_field_width or x1 < 0 or y1 >= playing_field_height or y1 < 0:
            game_CLOSE = True
        x1 += x1_change
        y1 += y1_change
        playing_field.fill(B)
        pygame.draw.rect(playing_field, Y, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        sn_hd = [x1, y1]
        SNAKE_List.append(sn_hd)
        if len(SNAKE_List) > Long_SNAKE:
            del SNAKE_List[0]

        for x in SNAKE_List[:-1]:
            if x == sn_hd:
                game_CLOSE = True

        snake(SNAKE_BLOCK, SNAKE_List)
        check(Long_SNAKE - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, playing_field_width - SNAKE_BLOCK) / 10.0) * 10.0
            foody = round(random.randrange(0, playing_field_height - SNAKE_BLOCK) / 10.0) * 10.0
            Long_SNAKE += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


gameLoop()
