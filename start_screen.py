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
    label_rect = Rectangle(WIDTH // 2 - 475, 25, 950, 120)

    # АВТОРЫ
    label_authors = Label(text='Создатели проекта: Денисов А., Касьянов К.', font_size=30, font='Times New Roman')

    # КНОПКИ ВЫБРАТЬ ИГРУ и ПРОЙТИ ТЕСТИРОВАНИЕ
    x1, y1, sx1, sy1 = WIDTH // 2 - 350, 180, 700, 200
    x2, y2, sx2, sy2 = WIDTH // 2 - 350, 430, 700, 200
    button1 = Rectangle(x1, y1, sx1, sy1)
    button2 = Rectangle(x2, y2, sx2, sy2)
    button_exit = Rectangle(20, HEIGHT - 70, 200, 60)

    bt1_label = Label('Выбрать игру', font_size=55, font='robo')
    bt2_label = Label('Пройти тестирование', font_size=55, font='robo')
    label_exit = Label('Выйти', font_size=40, font='robo')
    x, y = 0, 0

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

        # ОТРИСОВКА
        label_rect.draw(screen, WHITE)
        label_game.draw_text(screen, BLACK, (50, 50))
        label_authors.draw_text(screen, BLACK, (WIDTH - 600, HEIGHT - 50))

        button1.draw(screen, YELLOW)
        button2.draw(screen, ORANGE)
        button_exit.draw(screen, RED)
        label_exit.draw_text(screen, BLACK, (73, HEIGHT - 55))

        bt1_label.draw_text(screen, BLACK, (int(button1.x + 210), int(button1.y + 80)))
        bt2_label.draw_text(screen, BLACK, (int(button2.x + 150), int(button2.y + 80)))

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
