from pygame import *
from random import sample, shuffle, randint, choice
from time import time as tm
from core.config import *
from core.classes import Label, Rectangle, GameButton


# ФУНКЦИЯ ВЫБОРА УРОВНЯ СЛОЖНОСТИ
def choice_difficult():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_game = Label(text='Выберите уровень сложности', font_size=70, font_='robo')
    label_rect = Rectangle(x=(WIDTH // 2 - 400), y=10, x_size=800, y_size=100)

    # КНОПКИ
    level1_txt = Label(text='Легкий', font_size=70, font_='robo')
    level2_txt = Label(text='Средний', font_size=70, font_='robo')
    level3_txt = Label(text='Сложный', font_size=70, font_='robo')
    buttons = [GameButton(x=(WIDTH // 2 - 350), y=150, x_size=700, y_size=175),
               GameButton(x=(WIDTH // 2 - 350), y=350, x_size=700, y_size=175),
               GameButton(x=(WIDTH // 2 - 350), y=550, x_size=700, y_size=175)]

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    x, y = 0, 0
    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT:
                return None
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                return 5
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, BLACK, position=(0, 60), cntr_x=True)

        buttons[0].color = PALE_GREEN
        buttons[1].color = PALE_YELLOW
        buttons[2].color = PALE_RED

        if buttons[0].collidepoint(x, y):
            buttons[0].color = GREEN
        if buttons[1].collidepoint(x, y):
            buttons[1].color = YELLOW
        if buttons[2].collidepoint(x, y):
            buttons[2].color = RED

        buttons[0].draw(screen, buttons[0].color, color_border=BLACK)
        buttons[1].draw(screen, buttons[1].color, color_border=BLACK)
        buttons[2].draw(screen, buttons[2].color, color_border=BLACK)

        level1_txt.draw_text(screen, BLACK, position=(0, 238), cntr_x=True)
        level2_txt.draw_text(screen, BLACK, position=(0, 438), cntr_x=True)
        level3_txt.draw_text(screen, BLACK, position=(0, 638), cntr_x=True)

        if buttons[0].collidepoint(x_click, y_click):
            return 'easy'
        if buttons[1].collidepoint(x_click, y_click):
            return 'normal'
        if buttons[2].collidepoint(x_click, y_click):
            return 'hard'

        display.update()


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 1
def game_1(diff, cheats):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_time = Label(font_size=50, font_='robo')
    label_game = Label(text='Игра на внимательность', font_size=70, font_='robo')
    label_rect = Rectangle(x=(WIDTH // 2 - 350), y=10, x_size=700, y_size=100)

    nums = []
    buttons = []
    # КНОПКИ
    if diff == 'easy':
        count = 5
        buttons = [GameButton(x=(200 + i * 115), y=(150 + j * 115), x_size=120, y_size=120)
                   for j in range(count) for i in range(count)]
        nums: list = sample(range(1, count ** 2 + 1), count ** 2)
        for but in range(count ** 2):
            buttons[but].num = nums[but]
            buttons[but].is_used = False

    if diff == 'normal':
        count = 6
        buttons = [GameButton(x=(200 + i * 95), y=(150 + j * 95), x_size=100, y_size=100)
                   for j in range(count) for i in range(count)]
        nums = sample(range(1, count ** 2 + 1), count ** 2)
        for but in range(count ** 2):
            buttons[but].num = nums[but]
            buttons[but].is_used = False

    if diff == 'hard':
        count = 7
        buttons = [GameButton(x=(200 + i * 85), y=(120 + j * 85), x_size=90, y_size=90)
                   for j in range(count) for i in range(count)]
        nums = sample(range(1, count ** 2 + 1), count ** 2)
        for but in range(count ** 2):
            buttons[but].num = nums[but]
            buttons[but].is_used = False

    # ЦИФРЫ
    label_nums = []
    if diff == 'easy':
        for but in buttons:
            label_nums.append(Label(text=f'{but.num}', font_size=80, font_='robo'))
    else:
        for but in buttons:
            label_nums.append(Label(text=f'{but.num}', font_size=60, font_='robo'))

    # ФОН
    start_screen_image = transform.scale(image.load('./assets/start_screen.jpg'), (WIDTH, HEIGHT))

    x, y = 0, 0
    actually_num = count * count - 1 if cheats else 1
    if cheats:
        print(f'{actually_num=}')
    seconds: str = ''
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
            label_time.draw_text(screen, color_=WHITE, position=(20, HEIGHT - 60),
                                 cntr_x=False, text_=f"Времени прошло: {seconds} секунд")

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT:
                run = False
                return False
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
        label_game.draw_text(screen, color_=BLACK, position=(0, 60), cntr_x=True)

        for but in buttons:
            but.draw(screen, but.color)

        if diff == 'easy':
            for but in range(count ** 2):
                if 10 <= nums[but] < 100:
                    label_nums[but].draw_text(screen, color_=BLACK, position=(buttons[but].x + 30, buttons[but].y + 35))
                elif 0 <= nums[but] < 10:
                    label_nums[but].draw_text(screen, color_=BLACK, position=(buttons[but].x + 45, buttons[but].y + 35))

        elif diff == 'hard':
            for but in range(count ** 2):
                if 10 <= nums[but] < 100:
                    label_nums[but].draw_text(screen, color_=BLACK, position=(buttons[but].x + 20, buttons[but].y + 26))
                elif 0 <= nums[but] < 10:
                    label_nums[but].draw_text(screen, color_=BLACK, position=(buttons[but].x + 34, buttons[but].y + 26))
        else:
            for but in range(count ** 2):
                if 10 <= nums[but] < 100:
                    label_nums[but].draw_text(screen, color_=BLACK,
                                              position=(buttons[but].x + 25, buttons[but].y + 32.5))
                elif 0 <= nums[but] < 10:
                    label_nums[but].draw_text(screen, color_=BLACK,
                                              position=(buttons[but].x + 40, buttons[but].y + 32.5))

        if actually_num == count ** 2 + 1:
            return seconds

        display.update()


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 2
def game_2(diff, cheats):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_time = Label(font_size=50, font_='robo')
    label_game = Label(text='Игра на память', font_size=70, font_='robo')
    label_rect = Rectangle(x=(WIDTH // 2 - 350), y=10, x_size=700, y_size=100)

    # КНОПКИ
    if diff == 'easy':
        count = 4
        buttons = [GameButton(
            x=(300 + i * 100), y=(200 + j * 100), x_size=100, y_size=100, is_radius=False, is_found=False)
            for j in range(count) for i in range(count)]
        nums = list(range(1, ((count ** 2) // 2) + 1)) * 2
        shuffle(nums)
        for i in range(0, count ** 2):
            buttons[i].num = nums[i]
        for i in buttons:
            i.is_pressed = False

    if diff == 'normal':
        count = 6
        buttons = [GameButton(
            x=(200 + i * 100), y=(130 + j * 100), x_size=100, y_size=100, is_radius=False, is_found=False)
            for j in range(count) for i in range(count)]
        nums = list(range(1, ((count ** 2) // 2) + 1)) * 2
        shuffle(nums)

        for i in range(0, count ** 2):
            buttons[i].num = nums[i]
        for i in buttons:
            i.is_pressed = False

    if diff == 'hard':
        count = 8
        buttons = [GameButton(
            x=(200 + i * 75), y=(130 + j * 75), x_size=75, y_size=75, is_radius=False, is_found=False)
            for j in range(count) for i in range(count)]
        nums = list(range(1, ((count ** 2) // 2) + 1)) * 2
        shuffle(nums)

        for i in range(0, count ** 2):
            buttons[i].num = nums[i]
        for i in buttons:
            i.is_pressed = False
    # ЦИФРЫ
    label_nums = []
    if diff == 'hard':
        for but in buttons:
            label_nums.append(Label(text=f'{but.num}', font_size=50, font_='robo'))
    elif diff == 'easy':
        for but in buttons:
            label_nums.append(Label(text=f'{but.num}', font_size=75, font_='robo'))
    else:
        for but in buttons:
            label_nums.append(Label(text=f'{but.num}', font_size=75, font_='robo'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    clicked_buttons = []
    pressed_buttons = []
    seconds: str = ''
    start_time = tm()
    calculate_time = False
    start = False
    wait = 0
    nums_need_win = 2 if cheats else 16 if diff == 'easy' else 36 if diff == 'normal' else 64 if diff == 'hard' else 81
    if cheats:
        print(f'{nums_need_win=}')
    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)
        current_time = tm()

        if calculate_time:
            seconds = f'{(current_time - start_time):.2f}'
            label_time.draw_text(screen, color_=WHITE, position=(20, HEIGHT - 60),
                                 cntr_x=False, text_=f"Времени прошло: {seconds} секунд")

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT:
                run = False
                return False
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, color_=BLACK, position=(0, 60), cntr_x=True)

        for i, but in enumerate(buttons):
            if diff == 'hard':
                but.draw(screen, but.color_b, width_border=7)
            else:
                but.draw(screen, but.color_b, width_border=8)
            label_position = 0, 0
            if diff == 'hard':
                if 10 <= but.num < 100:
                    label_position = (but.x + 20, but.y + 22.5)
                elif 0 <= but.num < 10:
                    label_position = (but.x + 28, but.y + 22.5)
            else:
                if 10 <= but.num < 100:
                    label_position = (but.x + 22.5, but.y + 26)
                elif 0 <= but.num < 10:
                    label_position = (but.x + 35, but.y + 26)

            if but.collidepoint(x_click, y_click) and not but.is_found and \
                    not but.is_pressed and len(clicked_buttons) < 2:
                if not start:
                    start_time = tm()
                    calculate_time = start = True
                if wait <= 0 and len(clicked_buttons) == 1:
                    wait = tm()
                but.is_pressed = True
                clicked_buttons.append(but)

            if len(clicked_buttons) == 2 and tm() - wait >= 0.6:
                wait = 0
                if clicked_buttons[0].num == clicked_buttons[1].num and \
                        clicked_buttons[0] != clicked_buttons[1]:
                    clicked_buttons[0].color_b = LIGHT_GREEN
                    clicked_buttons[1].color_b = LIGHT_GREEN
                    clicked_buttons[0].is_found = True
                    clicked_buttons[1].is_found = True
                    pressed_buttons.append(clicked_buttons[0])
                    pressed_buttons.append(clicked_buttons[1])
                else:
                    clicked_buttons[0].color_b = YELLOW
                    clicked_buttons[1].color_b = YELLOW
                    clicked_buttons[0].is_pressed = False
                    clicked_buttons[1].is_pressed = False
                clicked_buttons.clear()

            if but.num == int(label_nums[i].text) and but.is_pressed:
                if not but.is_found:
                    but.color_b = LIGHT_GRAY
                label_nums[i].draw_text(screen, color_=BLACK, position=label_position)

        if len(pressed_buttons) == nums_need_win:
            return seconds
        display.update()


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 3
def game_3(diff, cheats):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_time = Label(font_size=50, font_='Arial Narrow')
    label_counter = Label(font_size=60, font_='Arial Narrow')
    label_game = Label(text='Игра на устный счёт', font_size=80, font_='Arial Narrow')
    label_rect = Rectangle(x=(WIDTH // 2 - 350), y=10, x_size=700, y_size=100)

    # ДОСКА
    board = Rectangle(x=0, y=150, x_size=750, y_size=250, relative_cntr_x=True)

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))
    start_time = tm()

    # DEFAULT VALUE
    is_decided = True
    x, y = 0, 0
    points_count: int = 0
    last_click_time: float = 0.0
    win = False
    any_but_pressed = False
    true_answer_text: str = ''
    buttons: list = []
    nums: list = []
    current_sign: str = ''
    answer: int = 0
    text_answers: list = []
    expression: Label = Label(text=f'', font_size=150, font_='Arial Narrow')
    color_expression = WHITE
    count = 1 if cheats else 10
    if cheats:
        print(f'{count=}')

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)
        current_time: float = tm()

        seconds: str = f'{(current_time - start_time):.2f}'
        label_time.draw_text(screen, color_=WHITE, position=(20, HEIGHT - 60),
                             cntr_x=False, text_=f"Времени прошло: {seconds} секунд")

        label_counter.draw_text(screen, color_=WHITE, position=(0, HEIGHT - 350),
                                text_=f'Количество очков: {points_count}/{count}', cntr_x=True)

        if is_decided and current_time - last_click_time >= 0.8:
            any_but_pressed = False
            color_expression = WHITE
            true_answer_text: str = ''

            if diff == 'easy':
                signs: list = ['+', '-']
                current_sign: str = signs[randint(0, 1)]

                if current_sign == '+':
                    nums: list = sorted([randint(1, 50), randint(1, 50)])
                    while int(str(nums[0])[-1]) + int(str(nums[1])[-1]) > 10:
                        nums: list = sorted([randint(1, 50), randint(1, 50)])

                if current_sign == '-':
                    nums: list = sorted([randint(1, 50), randint(1, 50)], reverse=True)
                    while int(str(nums[0])[-1]) < int(str(nums[1])[-1]):
                        nums: list = sorted([randint(1, 50), randint(1, 50)], reverse=True)

                answer: int = eval(f'{nums[0]}{current_sign}{nums[1]}')
                expression: Label = Label(text=f'{nums[0]} {current_sign} {nums[1]} = ', font_size=140,
                                          font_='Arial Narrow')
                if answer < 11:
                    variants: list = [answer, answer + randint(1, 7), answer + randint(1, 5), answer + randint(1, 10)]
                else:
                    variants: list = [answer, answer + randint(1, 7), answer - randint(1, 5), answer - randint(1, 10)]
                shuffle(variants)

            if diff == 'normal':
                signs: list = ['+', '-', '*']
                current_sign: str = signs[randint(0, 2)]
                if current_sign == '*':
                    nums: list = [choice([0, 1, 2, 3, 4, 5, 6, 7, 10]), choice([0, 1, 2, 3, 4, 5, 6, 7, 10])]
                if current_sign == '+':
                    nums: list = sorted([randint(30, 100), randint(1, 100)])
                    while int(str(nums[0])[-1]) + int(str(nums[1])[-1]) > 10:
                        nums: list = sorted([randint(30, 100), randint(1, 100)])

                if current_sign == '-':
                    nums: list = sorted([randint(30, 100), randint(1, 100)], reverse=True)
                    while int(str(nums[0])[-1]) < int(str(nums[1])[-1]):
                        nums: list = sorted([randint(30, 100), randint(1, 100)], reverse=True)

                answer: int = eval(f'{nums[0]}{current_sign}{nums[1]}')
                expression: Label = Label(text=f'{nums[0]} {current_sign} {nums[1]} = ', font_size=140,
                                          font_='Arial Narrow')
                if answer < 11:
                    variants: list = [answer, answer + randint(1, 7), answer + randint(1, 5), answer + randint(1, 10)]
                else:
                    variants: list = [answer, answer + randint(1, 7), answer - randint(1, 5), answer - randint(1, 10)]
                shuffle(variants)

            if diff == 'hard':
                signs: list = ['+', '-', '*']
                current_sign: str = signs[randint(0, 2)]
                if current_sign == '*':
                    nums: list = [randint(0, 25), randint(0, 10)]
                else:
                    nums: list = sorted([randint(30, 250), randint(10, 250)], reverse=True)
                answer: int = eval(f'{nums[0]}{current_sign}{nums[1]}')
                expression: Label = Label(text=f'{nums[0]} {current_sign} {nums[1]} = ', font_size=125,
                                          font_='Arial Narrow')
                if answer < 11:
                    variants: list = [answer, answer + randint(1, 7), answer + randint(1, 5), answer + randint(1, 10)]
                else:
                    variants: list = [answer, answer + randint(1, 7), answer - randint(1, 5), answer - randint(1, 10)]
                shuffle(variants)

            buttons: list = [
                GameButton(x=(140 + i * 180), y=500, x_size=180, y_size=180, is_radius=False, is_found=False)
                for i in range(4)]

            for i, button in enumerate(buttons):
                button.num = variants[i]

            text_answers: list = [Label(text=f'{i}', font_size=120, font_='Arial Narrow') for i in variants]
            is_decided = False
            if points_count >= count:
                win = True

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT:
                run = False
                return False
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, color_=BLACK, position=(0, 60), cntr_x=True)

        for i, but in enumerate(buttons):
            if not but.is_found:
                if but.collidepoint(x, y):
                    but.color_b = DARK_YELLOW
                else:
                    but.color_b = YELLOW

        for i, but in enumerate(buttons):
            if but.collidepoint(x_click, y_click) and not any_but_pressed:
                true_answer_text = str(eval(f'{nums[0]}{current_sign}{nums[1]}'))
                color_expression = LIGHT_GREEN
                any_but_pressed = True
                if answer == but.num:
                    points_count += 1
                    but.color_b = LIGHT_GREEN
                else:
                    points_count -= 1
                    but.color_b = RED
                but.is_found = True
                is_decided = True
                last_click_time = current_time

        for i, but in enumerate(buttons):
            but.draw(screen, but.color_b)
            label_position = 0, 0
            if 100 <= but.num < 1000:
                label_position = (but.x + 20, but.y + 53)
            elif 10 <= but.num < 100:
                label_position = (but.x + 43.5, but.y + 53)
            elif 0 <= but.num < 10:
                label_position = (but.x + 67.6, but.y + 53)
            text_answers[i].draw_text(screen, BLACK, label_position)

        board.draw(screen, SCHOOL_BOARD_COLOR, color_border=BROWN)
        expression.draw_text(screen, color_=color_expression, position=(205, 235),
                             text_=f'{nums[0]} {current_sign} {nums[1]} = {true_answer_text}')

        if points_count < 0:
            points_count = 0

        if win:
            return seconds

        display.update()
