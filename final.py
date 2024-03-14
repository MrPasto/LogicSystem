from pygame import *
from config import *
from classes import Label


def final_window(seconds):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    fin_label = Label(text=f'Поздравляем!//Ты справился за {seconds} секунд!', font_size=70,
                      font='times new roman')

    again_label = Label(text='Нажмите "Enter", чтобы продолжить', font_size=50,
                        font='times new roman')

    final_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    run = True
    while run:
        screen.blit(final_screen_image, (0, 0))
        clock.tick(FPS)

        for ev in event.get():
            # ВЫХОД
            if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                run = False
                return None
            # Возвращение на главный экран
            if ev.type == KEYDOWN and ev.key == K_RETURN:
                return 'yes'

        fin_label.draw_text(screen, color=BLACK, position=(-100, HEIGHT // 2 - 150), cntr_x=True)
        again_label.draw_text(screen, color=GRAY, position=(-100, HEIGHT // 2 + 100), cntr_x=True)

        display.update()
