"""Игра 'Reverse crosses and zeros'."""

from tkinter import *
from random import *
import time

window = Tk()
window.title('Reverse cross and zeros')
game = True
square = []
cross_count = 0
SIZE = 10
HALF = 5


def new_game():
    for x in range(SIZE):
        for y in range(SIZE):
            square[x][y]['text'] = ' '
            square[x][y]['background'] = 'orange'
    global game
    game = True
    global cross_count
    cross_count = 0


def press(x, y):
    if game and square[x][y]['text'] == ' ':
        square[x][y]['text'] = 'X'
        global cross_count
        cross_count += 1
        loose_check()
        if game and cross_count < SIZE ** 2 % 2 + SIZE ** 2 // 2:
            computer()
            loose_check()


def loose_check():
    for i in range(SIZE):
        for j in range(SIZE):
            try:
                line_check(square[i][j],
                           square[i][j + 1],
                           square[i][j + 2],
                           square[i][j + 3],
                           square[i][j + 4])

                line_check(square[j][i],
                           square[j + 1][i],
                           square[j + 2][i],
                           square[j + 3][i],
                           square[j + 4][i])

                line_check(square[i][j],
                           square[i - 1][j + 1],
                           square[i - 2][j + 2],
                           square[i - 3][j + 3],
                           square[i - 4][j + 4])

                line_check(square[i][j],
                           square[i + 1][j + 1],
                           square[i + 2][j + 2],
                           square[i + 3][j + 3],
                           square[i + 4][j + 4])
            except IndexError:
                continue


def line_check(a, b, c, d, e):
    if a['text'] == b['text'] == c['text'] == d['text'] == e['text'] != ' ':
        red(a, b, c, d, e)


def computer():
    while True:
        window.update()
        time.sleep(0.01)
        x = randint(0, SIZE - 1)
        y = randint(0, SIZE - 1)
        if square[x][y]['text'] == ' ':
            square[x][y]['text'] = 'O'
            break


def red(a, b, c, d, e):
    a['background'] = b['background'] = c['background'] = d['background'] = e['background'] = 'red'
    global game
    game = False


def close_window():
    window.destroy()


def start():
    for row in range(SIZE):
        line = []
        for col in range(SIZE):
            button = Button(window, text=' ', width=3, height=1,
                            font=('Verdana', 20, 'bold'),
                            background='orange',
                            command=lambda row=row, col=col: press(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        square.append(line)
    start_button = Button(window, text='начать', command=new_game)
    start_button.grid(row=SIZE, column=0, columnspan=HALF, sticky='nsew')
    quit_button = Button(window, text='выйти', command=close_window)
    quit_button.grid(row=SIZE, column=5, columnspan=SIZE, sticky='nsew')
    window.update()
    window.mainloop()


start()

