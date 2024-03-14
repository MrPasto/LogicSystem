from pygame import *
from config import *
from classes import Label, Rectangle


# ФУНКЦИЯ ЗАПУСКАЕТ СТАРТОВОЕ ОКНО
def start_screen():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    # ЗАГОЛОВОК
    label_game = Label(text='Развитие логического мышления', font_size=64, font='Times New Roman')
    label_rect = Rectangle(x=(WIDTH // 2 - 475), y=25, x_size=950, y_size=120)

    # АВТОРЫ
    label_authors = Label(text='Создатели проекта: Денисов А., Касьянов К.', font_size=30, font='Times New Roman')

    # КНОПКИ ВЫБРАТЬ ИГРУ и ПРОЙТИ ТЕСТИРОВАНИЕ
    x1, y1, sx1, sy1 = WIDTH // 2 - 350, 180, 700, 200
    x2, y2, sx2, sy2 = WIDTH // 2 - 350, 430, 700, 200
    button1 = Rectangle(x=x1, y=y1, x_size=sx1, y_size=sy1)
    button2 = Rectangle(x=x2, y=y2, x_size=sx2, y_size=sy2)
    button_exit = Rectangle(x=20, y=(HEIGHT - 70), x_size=200, y_size=60)

    bt1_label = Label(text='Выбрать игру', font_size=55, font='robo')
    bt2_label = Label(text='Пройти тестирование', font_size=55, font='robo')
    label_exit = Label(text='Выйти', font_size=40, font='robo')
    x, y, x_pos, y_pos = 0, 0, 0, 0

    # ФОН
    start_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    run = True
    while run:
        screen.blit(start_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫКЛЮЧЕНИЕ
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                run = False
            # ВЕРНУТЬ КООРДИНАТЫ НАЖАТИЯ МЫШКОЙ
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x, y = ev.pos
            if ev.type == MOUSEMOTION:
                x_pos, y_pos = ev.pos

        # ОТРИСОВКА
        # ПРИ НАВЕДЕНИИ НА КНОПКУ ОНА МЕНЯЕТ ЦВЕТ
        if button1.collidepoint(x_pos, y_pos):
            button1.draw(screen, DARK_YELLOW)
        else:
            button1.draw(screen, YELLOW)

        if button2.collidepoint(x_pos, y_pos):
            button2.draw(screen, DARK_ORANGE)
        else:
            button2.draw(screen, ORANGE)

        if button_exit.collidepoint(x_pos, y_pos):
            button_exit.draw(screen, DARK_RED, color_border=GRAY)
            label_exit.draw_text(screen, color=LIGHT_GRAY, position=(73, HEIGHT - 55))
        else:
            button_exit.draw(screen, RED)
            label_exit.draw_text(screen, color=BLACK, position=(73, HEIGHT - 55))

        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, color=BLACK, position=(50, 50))
        label_authors.draw_text(screen, color=BLACK, position=(WIDTH - 600, HEIGHT - 50))
        bt1_label.draw_text(screen, color=BLACK, position=(int(button1.x + 210), int(button1.y + 80)))
        bt2_label.draw_text(screen, color=BLACK, position=(int(button2.x + 150), int(button2.y + 80)))

        # НАЖАТИЯ ПО КНОПКАМ
        events = key.get_pressed()
        if button1.collidepoint(x, y):
            return 0

        if button2.collidepoint(x, y):
            return 1

        if button_exit.collidepoint(x, y):
            return None

        display.update()

# start_screen()
