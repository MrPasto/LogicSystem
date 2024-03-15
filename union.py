from start_screen import start_screen
from first_gamemode import first
from game_1 import game_1
from game_2 import game_2
from game_3 import game_3
from final import final_window


def none():
    return None


def union_functions():
    choice_window1 = {0: first, 1: none, None: none}
    choice_window3 = {1: game_2, 2: game_1, 3: game_3, 4: none, 5: union_functions, None: none}
    window1 = start_screen()
    window2 = choice_window1[window1]
    window3 = window2()
    window4 = choice_window3[window3]
    seconds = window4()
    if type(seconds) == str:
        print('final show')
        again = final_window(seconds)
        if again:
            union_functions()


def main():
    union_functions()
