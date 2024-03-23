import time

from pygame import *
from config import *
from classes import Label, Rectangle, GameButton
from random import randint
from random import shuffle
from time import time as tm


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 3
def game_3():
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
                                text_=f'Количество очков: {points_count}/{COUNT_3}', cntr_x=True)

        if is_decided and current_time - last_click_time >= 0.8:
            any_but_pressed = False
            color_expression = WHITE
            signs: list = ['+', '-', '*']
            current_sign: str = signs[randint(0, 2)]
            if current_sign == '*':
                nums: list = [randint(1, 25), randint(0, 3)]
            else:
                nums: list = sorted([randint(1, 100), randint(1, 100)], reverse=True)
            expression: Label = Label(text=f'{nums[0]} {current_sign} {nums[1]} = ', font_size=150,
                                      font_='Arial Narrow')
            answer: int = eval(f'{nums[0]}{current_sign}{nums[1]}')
            true_answer_text: str = ''
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
            if points_count >= COUNT_3:
                win = True

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

# print(game_3())
