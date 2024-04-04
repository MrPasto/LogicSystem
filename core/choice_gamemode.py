from pygame import *
from core.config import *
from core.classes import Label, Rectangle
from core.games import game_1, game_2, game_3


# ФУНКЦИЯ ЗАПУСКАЕТ МЕНЮ ВЫБОРА ИГРЫ
def first():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # КНОПКИ
    x1, y1, sx1, sy1 = -300, 50, 275, 275
    x2, y2, sx2, sy2 = 0, 50, 275, 275
    x3, y3, sx3, sy3 = 300, 50, 275, 275
    buttons = [Rectangle(x=x1, y=y1, x_size=sx1, y_size=sy1, relative_cntr_x=True, relative_cntr_y=True),
               Rectangle(x=x2, y=y2, x_size=sx2, y_size=sy2, relative_cntr_x=True, relative_cntr_y=True),
               Rectangle(x=x3, y=y3, x_size=sx3, y_size=sy3, relative_cntr_x=True, relative_cntr_y=True), ]

    x5, y5, sx5, sy5 = 0, 550, 300, 125
    choice_button = Rectangle(x=x5, y=y5, x_size=sx5, y_size=sy5, relative_cntr_x=True)
    label_choice_game = Label(text='Выбрать', rect_=choice_button, font_size=70, font_='robo')

    label_rect = Rectangle(x=250, y=5, x_size=500, y_size=100)
    label_choice = Label(text='Выберите игру', font_size=70, font_='robo')

    labels_game = [
        Label(text='Игра на//внима-//тельность', rect_=buttons[0], font_size=70, font_='robo'),
        Label(text='Игра на//память', rect_=buttons[1], font_size=70, font_='robo'),
        Label(text='Игра на//устный//счёт', rect_=buttons[2], font_size=70, font_='robo'),
    ]

    button_exit = Rectangle(x=20, y=HEIGHT - 70, x_size=200, y_size=60)
    label_exit = Label(text='Назад', font_size=40, font_='robo')

    x_click, y_click, x, y = 0, 0, 0, 0

    # ФОН
    choose_screen_image = transform.scale(image.load('./assets/start_screen.jpg'), (WIDTH, HEIGHT))

    choice_string = ''

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        screen.blit(choose_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫХОД
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                return None
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_choice.draw_text(screen, color_=BLACK, position=(0, 55), cntr_x=True)

        button_exit.draw(screen, LIGHT_GRAY)
        label_exit.draw_text(screen, color_=BLACK, position=(73, HEIGHT - 55))

        # ПРИ НАВЕДЕНИИ НА КНОПКУ ОНА МЕНЯЕТ ЦВЕТ
        for i, button in enumerate(buttons):
            if button.collidepoint(x, y):
                button.draw(screen, DARK_YELLOW)
            else:
                button.draw(screen, YELLOW)

            if button_exit.collidepoint(x, y):
                button_exit.draw(screen, GRAY)
                label_exit.draw_text(screen, color_=LIGHT_GRAY, position=(73, HEIGHT - 55))

        if choice_string:
            if choice_button.collidepoint(x, y):
                choice_button.draw(screen, DARK_ORANGE)
            else:
                choice_button.draw(screen, ORANGE)
            label_choice_game.draw_text(screen, color_=BLACK, position=(0, 705), cntr_x=True)

            if choice_button.collidepoint(x_click, y_click):
                return int(choice_string[-1])

        # НАЖАТИЯ ПО КНОПКАМ
        for i, but in enumerate(buttons):
            if but.collidepoint(x_click, y_click):
                choice_string += str(i + 1)
                x_click, y_click = 0, 0
                button_pressed = but

        try:
            button_pressed.draw(screen, LIGHT_GREEN)
        except UnboundLocalError:
            ...
        for i, button in enumerate(buttons):
            labels_game[i].draw_text(screen, color_=BLACK,
                                     position=(button.rect.x + 20, button.rect.y + 20), cntr_x=True)

        if button_exit.collidepoint(x_click, y_click):
            return 5

        display.update()


def second(diff):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()
    game1_seconds = game_1(diff)
    if game1_seconds:
        game2_seconds = game_2(diff)
        if game2_seconds:
            game3_seconds = game_3(diff)
            return game1_seconds, game2_seconds, game3_seconds
