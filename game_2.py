from pygame import *
from config import *
from classes import Label, Rectangle, Game1Button
from random import randint, sample, shuffle
from time import time as tm


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 2

def game_2():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_time = Label(font_size=35, font='Times New Roman')
    label_game = Label(text='Игра на память', font_size=64, font='Times New Roman')
    label_rect = Rectangle(WIDTH // 2 - 350, 10, 700, 100)

    # КНОПКИ
    buttons = [Game1Button(200 + i * 95, 150 + j * 95, 100, 100) for j in range(COUNT_2) for i in range(COUNT_2)]
    nums_1 = sample(range(1, ((COUNT_2 ** 2) // 2) + 1), (COUNT_2 ** 2) // 2)
    nums_2 = nums_1[:]
    shuffle(nums_2)
    nums_1.extend(nums_2)
    for i in range(0, COUNT_2 ** 2):
        buttons[i].num = nums_1[i]
    for i in buttons:
        i.is_used = False

    # ЦИФРЫ
    label_nums = []
    for but in buttons:
        label_nums.append(Label(text=f'{but.num}', font_size=40, font='Times New Roman'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    x, y = 0, 0
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

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, BLACK, (0, 55), cntr_x=True)
        for but in buttons:
            if not (but.is_used):
                but.draw(screen, YELLOW)

        for but in buttons:
            if but.collidepoint(x_click, y_click):
                for lab in label_nums:
                    if but.num == int(lab.text):
                        lab.draw_text(screen, BLACK, (but.x + 30, but.y + 30))
                        but.is_used = True

        for but in buttons:
            for lab in label_nums:
                if but.num == int(lab.text) and but.is_used:
                    but.draw(screen, YELLOW)
                    lab.draw_text(screen, BLACK, (but.x + 30, but.y + 30))
                

        display.update()


game_2()
