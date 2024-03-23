from pygame import *
from config import *
from classes import Label


def final_window(seconds, gamemode_number):
    init()

    screen = display.set_mode(SCREEN_SIZE)
    display.set_caption('Nice game')
    clock = time.Clock()

    final_screen_image = transform.scale(image.load('assets/start_screen.jpg'), (WIDTH, HEIGHT))

    if gamemode_number == 0:

        fin_label = Label(text=f'Поздравляем!////Ты справился за {seconds} секунд!', font_size=80,
                          font_='robo')

        again_label = Label(text='Нажми "Enter", чтобы продолжить', font_size=60,
                            font_='robo')

        run = True
        while run:
            screen.blit(final_screen_image, (0, 0))
            clock.tick(FPS)

            for ev in event.get():
                # ВЫХОД
                if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                    return None
                # Возвращение на главный экран
                if ev.type == KEYDOWN and (ev.key == K_RETURN or ev.key == K_KP_ENTER):
                    return 'yes'

            fin_label.draw_text(screen, color_=BLACK, position=(0, HEIGHT // 2 - 150), cntr_x=True)
            again_label.draw_text(screen, color_=GRAY, position=(0, HEIGHT // 2 + 100), cntr_x=True)

            display.update()

    else:
        seconds_ = [float(second) for second in seconds]
        sum_seconds = round(sum(seconds_), 10)

        fin_label = Label(text=f'Поздравляем!////Ты прошёл тестирование!',
                          font_size=80, font_='robo')

        res_label = Label(
            text=f'Ты прошел//игру на внимательность за {seconds[0]} секунд,//игру на память за {seconds[1]} '
                 f'секунд//и игру на устный счёт за {seconds[2]} секунд.',
            font_size=60, font_='robo')
        main_result_label = Label(text=f'Итоговый результат - {sum_seconds} секунд.',
                                  font_size=60, font_='robo')

        again_label = Label(text='Нажми "Enter", чтобы продолжить',
                            font_size=50, font_='robo', italiano=True)

        run = True
        while run:
            screen.blit(final_screen_image, (0, 0))
            clock.tick(FPS)

            for ev in event.get():
                # ВЫХОД
                if ev.type == QUIT or ev.type == KEYDOWN and ev.key == K_ESCAPE:
                    return None, seconds_
                # Возвращение на главный экран
                if ev.type == KEYDOWN and (ev.key == K_RETURN or ev.key == K_KP_ENTER):
                    return [seconds_]

            fin_label.draw_text(screen, color_=BLACK, position=(0, HEIGHT // 2 - 300), cntr_x=True)

            res_label.draw_text(screen, color_=BLACK, position=(0, HEIGHT // 2 - 100), cntr_x=True)
            main_result_label.draw_text(screen, color_=BLACK, position=(0, HEIGHT // 2 + 150), cntr_x=True)

            again_label.draw_text(screen, color_=GRAY, position=(0, HEIGHT // 2 + 300), cntr_x=True)

            display.update()
