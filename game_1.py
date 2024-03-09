from pygame import *
from config import *
from classes import Label, Rectangle, GameButton
from random import sample
from time import time as tm


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 1

def game_1():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_time = Label(font_size=35, font='Times New Roman')
    label_game = Label(text='Игра на внимательность', font_size=64, font='Times New Roman')
    label_rect = Rectangle(WIDTH // 2 - 350, 10, 700, 100)

    # КНОПКИ
    buttons = [GameButton(200 + i * 95, 150 + j * 95, 100, 100) for j in range(COUNT) for i in range(COUNT)]
    nums = sample(range(1, COUNT ** 2 + 1), COUNT ** 2)
    for but in range(COUNT ** 2):
        buttons[but].num = nums[but]
        buttons[but].is_used = False

    # ЦИФРЫ
    label_nums = []
    for but in buttons:
        label_nums.append(Label(text=f'{but.num}', font_size=40, font='Times New Roman'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    x, y = 0, 0
    actually_num = 35
    seconds = 0
    calculate_time = False
    start_time = tm()
    start = False

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

        current_time = tm()
        if calculate_time:
            seconds = f'{(current_time - start_time):.2f}'
            label_time.draw_text(screen, WHITE, (20, HEIGHT - 60),
                                 cntr_x=False, text_=f"Времени прошло: {seconds} секунд")

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                run = False
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # НАЖАТИЕ ПО КНОПКАМ И ОСНОВНАЯ МЕХАНИКА
        for i, but in enumerate(buttons):
            if but.collidepoint(x_click, y_click):
                if not start:
                    start_time = tm()
                    start = True
                calculate_time = True
                if but.num == actually_num:
                    but.is_used = True
                    actually_num += 1
                    but.color = LIGHT_GREEN

        # СМЕНА ЦВЕТА ПРИ НАВЕДЕНИИ НА КНОПКУ
        for but in buttons:
            if but.collidepoint(x, y) and not but.is_used:
                but.color = DARK_YELLOW
            elif not but.is_used:
                but.color = YELLOW

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, BLACK, (0, 55), cntr_x=True)

        for but in buttons:
            but.draw(screen, but.color)
        for but in range(COUNT ** 2):
            if 10 <= nums[but] < 100:
                label_nums[but].draw_text(screen, BLACK, (buttons[but].x + 30, buttons[but].y + 30))
            elif 0 <= nums[but] < 10:
                label_nums[but].draw_text(screen, BLACK, (buttons[but].x + 40, buttons[but].y + 30))

        if actually_num == COUNT ** 2 + 1:
            return seconds

        display.update()

# game_1()
