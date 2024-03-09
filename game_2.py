from pygame import *
from config import *
from classes import Label, Rectangle, GameButton
from random import sample, shuffle
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
    buttons = [GameButton(200 + i * 100, 150 + j * 100, 100, 100, is_radius=False, is_found=False)
               for j in range(COUNT_2) for i in range(COUNT_2)]
    nums_1 = sample(range(1, ((COUNT_2 ** 2) // 2) + 1), (COUNT_2 ** 2) // 2)
    nums_2 = nums_1[:]
    shuffle(nums_2)
    nums_3 = [0] * ((COUNT_2 ** 2) // 2)
    nums_1.extend(nums_2)
    nums_2 = nums_3 + nums_2
    for i in range(0, COUNT_2 ** 2):
        buttons[i].num = nums_1[i]
    for i in buttons:
        i.is_used = False
    print(nums_1)
    print(nums_2)
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

    clicked_buttons = []

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

        for i, but in enumerate(buttons):
            but.draw(screen, YELLOW)

            if but.is_found:
                but.draw(screen, LIGHT_GREEN)

            for label in label_nums:
                if but.collidepoint(x_click, y_click) and but.num == int(label.text) and not but.is_used:
                    but.is_used = True
                    clicked_buttons.append(but.num)
                    print(clicked_buttons)
                    x_click, y_click = 0, 0

                if but.num == int(label.text) and but.is_used:
                    if 10 <= but.num < 100:
                        label.draw_text(screen, BLACK, (but.x + 30, but.y + 30))
                    elif 0 <= but.num < 10:
                        label.draw_text(screen, BLACK, (but.x + 40, but.y + 30))

            if len(clicked_buttons) == 2:
                if clicked_buttons[0] == clicked_buttons[1]:
                    buttons[nums_1.index(clicked_buttons[0])].is_found = True
                    buttons[nums_2.index(clicked_buttons[1])].is_found = True
                else:
                    buttons[nums_1.index(clicked_buttons[0])].is_used = False
                    buttons[nums_1.index(clicked_buttons[1])].is_used = False
                    buttons[nums_2.index(clicked_buttons[0])].is_used = False
                    buttons[nums_2.index(clicked_buttons[1])].is_used = False
                clicked_buttons.clear()

        display.update()


game_2()
