#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют
цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета.
"""
from tkinter import *


class MyButton:
    def __init__(self, color):
        Button(
            width=23,
            bg=color,
            command=lambda: change(color)
        ).pack(padx=6)


def change(color):
    if color == "#ff0000":
        lab['text'] = "Красный"
    elif color == "#ff7d00":
        lab['text'] = "Оранжевый"
    elif color == "#ffff00":
        lab['text'] = "Жёлтый"
    elif color == "#00ff00":
        lab['text'] = "Зелёный"
    elif color == "#007dff":
        lab['text'] = "Голубой"
    elif color == "#0000ff":
        lab['text'] = "Синий"
    elif color == "#7d00ff":
        lab['text'] = "Фиолетовый"
    ent.delete(0, END)
    ent.insert(0, color)


if __name__ == '__main__':
    root = Tk()
    # Текст
    lab = Label(width=20)
    lab.pack(padx=6)
    # Поле
    ent = Entry(width=20)
    ent.pack(padx=6)
    # Кнопки
    but1 = MyButton("#ff0000")
    but2 = MyButton("#ff7d00")
    but3 = MyButton("#ffff00")
    but4 = MyButton("#00ff00")
    but5 = MyButton("#007dff")
    but6 = MyButton("#0000ff")
    but7 = MyButton("#7d00ff")

    root.mainloop()
