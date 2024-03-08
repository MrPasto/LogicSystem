from pygame import *
from config import *
from classes import Label, Rectangle
from random import randint, sample

# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 1

def game_1():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_game = Label(text='Развитие логического мышления', font_size=64, font='Times New Roman')
    label_rect = Rectangle(WIDTH // 2 - 475, 25, 950, 120)

    #КНОПКИ
    buttons = [Rectangle(200 + i*95, 150 +j*95, 100, 100) for j in range(count) for i in range(count)]
    nums = sample(range(1,count**2+1), count**2)
    for i in range(count**2):
        buttons[i].num = nums[i]

    # ЦИФРЫ
    label_nums = []
    for i in buttons:
        label_nums.append(Label(text=f'{i.num}', font_size= 40, font='Times New Roman'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    run = True
    while run:
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                run = False
            # ВЕРНУТЬ КООРДИНАТЫ НАЖАТИЯ МЫШКОЙ
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x, y = ev.pos

        # ОТРИСОВКА
        for i in buttons:
            i.draw(screen,YELLOW)
        a = 0
        for i in range(count**2):
            label_nums[i].draw_text(screen, BLACK, (buttons[i].x + 30, buttons[i].y + 30))


        display.update()


game_1()
