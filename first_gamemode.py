from pygame import *
from config import *
from classes import Label, Rectangle


# ФУНКЦИЯ ЗАПУСКАЕТ МЕНЮ ВЫБОРА ИГРЫ
def first():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    label_rect = Rectangle(250, 5, 500, 100)
    label_choice = Label(text='Выберите игру', font_size=40, font='Times New Roman')

    labels_game = [
        Label(text='Игра на/память', font_size=50, font='robo'),
        Label(text='Игра на/внимате-/льность', font_size=50, font='robo'),
        Label(text='Игра на ...', font_size=50, font='robo'),
        Label(text='Игра на ...', font_size=50, font='robo'),
    ]

    # КНОПКИ
    x1, y1, sx1, sy1 = 150, 150, 200, 200
    x2, y2, sx2, sy2 = -150, 150, 200, 200
    x3, y3, sx3, sy3 = -150, -100, 200, 200
    x4, y4, sx4, sy4 = 150, -100, 200, 200
    buttons = [Rectangle(x1, y1, sx1, sy1, relative_cntr_x=True, relative_cntr_y=True),
               Rectangle(x2, y2, sx2, sy2, relative_cntr_x=True, relative_cntr_y=True),
               Rectangle(x3, y3, sx3, sy3, relative_cntr_x=True, relative_cntr_y=True),
               Rectangle(x4, y4, sx4, sy4, relative_cntr_x=True, relative_cntr_y=True)]
    b1, b2, b3, b4 = buttons[0], buttons[1], buttons[2], buttons[3]

    x5, y5, sx5, sy5 = 0, 655, 250, 100
    choice_button = Rectangle(x5, y5, sx5, sy5, relative_cntr_x=True)
    label_choice_game = Label(text='Выбрать', font_size=60, font='Times New Roman')

    x_click, y_click, x, y = 0, 0, 0, 0

    # ФОН
    choose_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        screen.blit(choose_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫХОД
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                run = False
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_choice.draw_text(screen, BLACK, (50, 50), cntr_x=True)

        # ПРИ НАВЕДЕНИИ НА КНОПКУ ОНА МЕНЯЕТ ЦВЕТ
        for i, button in enumerate(buttons):
            if button.collidepoint(x, y):
                button.draw(screen, DARK_YELLOW)
            else:
                button.draw(screen, YELLOW)
            labels_game[i].draw_text(screen, BLACK, (button.rect.x + 20, button.rect.y + 20))

        if choice_button.collidepoint(x, y):
            choice_button.draw(screen, DARK_ORANGE)
        else:
            choice_button.draw(screen, ORANGE)

        label_choice_game.draw_text(screen, BLACK, (100, 705), cntr_x=True)

        # НАЖАТИЯ ПО КНОПКАМ
        for i, but in enumerate(buttons):
            if but.collidepoint(x_click, y_click):
                print(i + 1)
                x_click, y_click = 0, 0

        if choice_button.collidepoint(x_click, y_click):
            print(5)
            x_click, y_click = 0, 0

        display.update()


first()
