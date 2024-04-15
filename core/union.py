from core.start_screen import start_screen
from core.choice_gamemode import first, second
from core.games import game_1, game_2, game_3, choice_difficult
from core.rules import rules
from core.final import final_window
from datetime import datetime


def none():
    return None


def union_functions() -> None:
    choice_window1 = {0: first, 1: none, 2: rules, None: none}
    choice_window3 = {1: game_1, 2: game_2, 3: game_3, 4: none, 5: union_functions, None: none}
    window1 = start_screen()
    cheats = window1[-1]
    if window1[0] == 0:
        seconds = 0
        window2 = choice_window1[window1[0]]
        window3 = window2()
        window4 = choice_window3[window3]
        if window4 == game_1 or window4 == game_2 or window4 == game_3:
            difficult = choice_difficult()
            if difficult == 5:
                union_functions()
            elif difficult:
                seconds = window4(difficult, cheats)
        elif window4 == union_functions:
            seconds = window4()
        if type(seconds) == str:
            print('final show')
            again = final_window(seconds, 0)
            if again:
                union_functions()
    elif window1[0] == 1:
        difficult = choice_difficult()
        if difficult == 5:
            union_functions()
        seconds = second(difficult, cheats)
        if seconds:
            again = final_window(seconds, 1)
            with open('./result.txt', 'a+', encoding='utf-8') as file:
                file.write(
                    f'{datetime.now():%d.%m.%Y %H:%M:%S}\n'
                    f'Уровень сложности: {difficult};\n'
                    f'Первая игра - {again[-1][0]} секунд,\n'
                    f'Вторая игра - {again[-1][1]} секунд,\n'
                    f'Третья игра - {again[-1][2]} секунд,\n'
                    f'Итоговое время - {round(sum(again[-1]), 10)} секунд.\n')
                file.write('\n')
            if again[0]:
                union_functions()

    elif window1[0] == 2:
        if rules() == 5:
            union_functions()


def main():
    union_functions()
