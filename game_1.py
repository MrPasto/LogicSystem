from pygame import *
from config import *
from classes import Label, Rectangle, Game1Button
from random import randint, sample


# ФУНКЦИЯ ЗАПУСКАЕТ ИГРУ 1

def game_1():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_game = Label(text='Игра на внимательность', font_size=64, font='Times New Roman')
    label_rect = Rectangle(WIDTH // 2 - 350, 10, 700, 100)

    # КНОПКИ
    buttons = [Game1Button(200 + i * 95, 150 + j * 95, 100, 100) for j in range(COUNT) for i in range(COUNT)]
    nums = sample(range(1, COUNT ** 2 + 1), COUNT ** 2)
    for i in range(COUNT ** 2):
        buttons[i].num = nums[i]
        buttons[i].ussed = False
    # ЦИФРЫ
    label_nums = []
    for i in buttons:
        label_nums.append(Label(text=f'{i.num}', font_size=40, font='Times New Roman'))

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    x, y = 0, 0
    actually_num = 1

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        x_click, y_click = 0, 0
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

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
        for i in buttons:
            if i.collidepoint(x_click, y_click):
                if i.num == actually_num:
                    i.ussed = True
                    actually_num += 1
                    print('YES')
                    i.color = LIGHT_GREEN
                else:
                    print('NO')

        # ПРИ НАВЕДЕНИИ НА КНОПКУ ОНА МЕНЯЕТ ЦВЕТ
        for i in buttons:
            if i.collidepoint(x, y) and not (i.ussed):
                i.color = DARK_YELLOW
            else:
                if not (i.ussed):
                    i.color = YELLOW

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, BLACK, (0, 55), cntr_x=True)

        for i in buttons:
            i.draw(screen, i.color)
        for i in range(COUNT ** 2):
            label_nums[i].draw_text(screen, BLACK, (buttons[i].x + 30, buttons[i].y + 30))

        display.update()


game_1()
