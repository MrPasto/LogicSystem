from pygame import *
from config import *
from classes import Label, Rectangle, GameButton
from random import shuffle
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
    nums = list(range(1, ((COUNT_2 ** 2) // 2) + 1)) * 2
    shuffle(nums)

    for i in range(0, COUNT_2 ** 2):
        buttons[i].num = nums[i]
    for i in buttons:
        i.is_pressed = False
    # ЦИФРЫ
    label_nums = []
    for but in buttons:
        label_nums.append(Label(text=f'{but.num}', font_size=40, font='Times New Roman'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    clicked_buttons = []
    start_time = current_time = tm()
    calculate_time = False

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

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
            # if current_time - start_time >= 1:
            #     if but.is_pressed and not but.is_found:
            #         but.color_b = YELLOW
            but.draw(screen, but.color_b)

            if 10 <= but.num < 100:
                label_position = (but.x + 30, but.y + 30)
            elif 0 <= but.num < 10:
                label_position = (but.x + 40, but.y + 30)

            if but.collidepoint(x_click, y_click) and not but.is_found and not but.is_pressed:
                but.is_pressed = True
                clicked_buttons.append(but)

            if len(clicked_buttons) == 2:
                if clicked_buttons[0].num == clicked_buttons[1].num and \
                        clicked_buttons[0] != clicked_buttons[1]:
                    clicked_buttons[0].color_b = LIGHT_GREEN
                    clicked_buttons[1].color_b = LIGHT_GREEN
                    clicked_buttons[0].is_found = True
                    clicked_buttons[1].is_found = True
                else:
                    clicked_buttons[0].color_b = YELLOW
                    clicked_buttons[1].color_b = YELLOW
                    clicked_buttons[0].is_pressed = False
                    clicked_buttons[1].is_pressed = False
                print(clicked_buttons[0].num, clicked_buttons[1].num)
                clicked_buttons.clear()

            if but.num == int(label_nums[i].text) and but.is_pressed:
                if not but.is_found:
                    but.color_b = LIGHT_GRAY
                label_nums[i].draw_text(screen, BLACK, label_position)

        display.update()


game_2()
