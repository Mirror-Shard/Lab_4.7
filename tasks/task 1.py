#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
Результат вычисления должен отображаться в метке.
Если арифметическое действие выполнить невозможно (например, если были введены
буквы, а не числа), то в метке должно появляться слово "ошибка".
"""
from tkinter import *


def sum():
    lab['text'] = float(a.get()) + float(b.get())


def sub():
    lab['text'] = float(a.get()) - float(b.get())


def mul():
    lab['text'] = float(a.get()) * float(b.get())


def div():
    lab['text'] = float(a.get()) / float(b.get())


if __name__ == '__main__':
    root = Tk()
    a = Entry(width=12)
    a.pack()
    b = Entry(width=12)
    b.pack()

    Button(text='+', width=15, command=sum).pack(padx=4)
    Button(text='-', width=15, command=sub).pack(padx=4)
    Button(text='*', width=15, command=mul).pack(padx=4)
    Button(text='/', width=15, command=div).pack(padx=4)

    lab = Label(width=10)
    lab.pack(padx=4)
    root.mainloop()
