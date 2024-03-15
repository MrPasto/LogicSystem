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
    label_time = Label(font_size=35, font='Times New Roman')
    label_game = Label(text='Игра на устный счёт', font_size=64, font='Times New Roman')
    label_rect = Rectangle(x=(WIDTH // 2 - 350), y=10, x_size=700, y_size=100)

    # ДОСКА
    doska = Rectangle(x=0, y=150, x_size=650, y_size=250, relative_cntr_x=True)

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    reshil = True
    x, y = 0, 0
    curent_count = 0
    start_time = current_time = tm()
    wait = 0
    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)
        current_time = tm()

        seconds = f'{(current_time - start_time):.2f}'
        label_time.draw_text(screen, color=WHITE, position=(20, HEIGHT - 60),
                             cntr_x=False, text_=f"Времени прошло: {seconds} секунд")

        if reshil:
            nums = [randint(1, 100), randint(1, 100)]
            nums.sort(reverse=True)
            znaki = ['+', '-']
            curent_znak = znaki[randint(0, 1)]
            primer = Label(text=f'{nums[0]} {curent_znak} {nums[1]} = ', font_size=100, font='Arial')
            ans = eval(f'{nums[0]}{curent_znak}{nums[1]}')
            varianti = [ans, ans + randint(1, 7), abs(ans - randint(1, 5)), abs(ans - randint(1, 10))]
            shuffle(varianti)
            ans_rect = [GameButton(x=(150 + i * 180), y=(500), x_size=180, y_size=180, is_radius=False, is_found=False)
                        for i in range(4)]

            for i, but in enumerate(ans_rect):
                but.num = varianti[i]

            ans_text = [Label(text=f'{i}', font_size=80, font='Arial') for i in varianti]
            reshil = False

        for i in ans_rect:
            i.color_b = YELLOW

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
        label_game.draw_text(screen, color=BLACK, position=(0, 55), cntr_x=True)

        doska.draw(screen, DARK_GREEN)
        primer.draw_text(screen, WHITE, (-100, 270), cntr_x=True)

        for i in ans_rect:
            if i.collidepoint(x, y):
                i.color_b = DARK_YELLOW
            if i.collidepoint(x_click, y_click):
                if ans == i.num:
                    curent_count += 1
                    i.color_b = LIGHT_GREEN
                    reshil = True
                else:
                    curent_count -= 1
                    i.color_b = RED
                    reshil = True

        for i, but in enumerate(ans_rect):
            but.draw(screen, but.color_b)
            ans_text[i].draw_text(screen, BLACK, (but.x + 40, but.y + 40))
        if reshil:
            time.wait(500)

        # if curent_count == COUNT_3:
        #     return seconds

        display.update()


game_3()
