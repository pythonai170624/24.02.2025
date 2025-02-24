
from days import *
from levels import *

def calc_day(day: Days):
    print(day)
    if day == Days.SUNDAY:
        print('yom rishon')

calc_day(Days.SUNDAY)

def play_game(level : Levels):
    print(level)
    if level == Levels.HARD:
        print('wow !')

play_game(Levels.HARD)

print(Levels.HARD.value[0])