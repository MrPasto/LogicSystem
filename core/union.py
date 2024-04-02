from LogicSystem.core.start_screen import start_screen
from LogicSystem.core.choice_gamemode import first, second
from LogicSystem.core.games import game_1, game_2, game_3
from LogicSystem.core.final import final_window
from datetime import datetime


def none():
    return None


def union_functions():
    choice_window1 = {0: first, 1: none, None: none}
    choice_window3 = {1: game_1, 2: game_2, 3: game_3, 4: none, 5: union_functions, None: none}
    window1 = start_screen()
    if window1 == 0:
        window2 = choice_window1[window1]
        window3 = window2()
        window4 = choice_window3[window3]
        seconds = window4()
        if type(seconds) == str:
            print('final show')
            again = final_window(seconds, 0)
            if again:
                union_functions()
    elif window1 == 1:
        seconds = second()
        if seconds:
            again = final_window(seconds, 1)
            with open('./result.txt', 'a+', encoding='utf-8') as file:
                file.write(
                    f'{datetime.now():%d.%m.%Y %H:%M:%S}\n'
                    f'Первая игра - {again[-1][0]} секунд,\n'
                    f'Вторая игра - {again[-1][1]} секунд,\n'
                    f'Третья игра - {again[-1][2]} секунд,\n'
                    f'Итоговое время - {round(sum(again[-1]), 10)} секунд.\n')
                file.write('\n')
            if again[0]:
                union_functions()


def main():
    union_functions()
