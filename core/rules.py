from pygame import *
from core.config import *
from core.classes import Label, Rectangle


# ПРАВИЛА ИГРЫ

def rules():
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Logic System')
    clock = time.Clock()

    button_exit = Rectangle(x=10, y=HEIGHT - 65, x_size=170, y_size=55)
    label_exit = Label(text='Назад', font_size=40, font_='robo')
    # ФОН
    choose_screen_image = transform.scale(image.load('./assets/tutor.png'), (WIDTH, HEIGHT))

    x_click, y_click = 0, 0
    # ИГРОВОЙ ЦИКЛ
    run = True
    while run:
        screen.blit(choose_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫХОД
            if ev.type == QUIT:
                return None
            # ОТСЛЕЖИВАНИЕ МЫШИ
            if ev.type == MOUSEMOTION:
                x, y = ev.pos
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                x_click, y_click = ev.pos
            if ev.type == KEYDOWN and ev.key == K_ESCAPE:
                return 5

        button_exit.draw(screen, LIGHT_GRAY)
        label_exit.draw_text(screen, color_=BLACK, position=(50, HEIGHT - 50))
        if button_exit.collidepoint(x_click, y_click):
            return 5

        display.update()
