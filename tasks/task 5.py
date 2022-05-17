#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Виджеты Radiobatton и Checkbutton поддерживают большинство свойств оформления
внешнего вида, которые есть у других элементов графического интерфейса.
При этом у Radiobutton есть особое свойство indicatoron. По-умолчанию он равен
единице, в этом случае радиокнопка выглядит как нормальная радиокнопка.
Однако если присвоить этой опции ноль, то виджет Radiobutton становится
похожим на обычную кнопку по внешнему виду. Но не по смыслу.
Напишите программу, в которой имеется несколько объединенных в группу
радиокнопок, индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь
кнопка включается, то в метке должна отображаться соответствующая ей
информация. Обычных кнопок в окне быть не должно.
"""
from tkinter import *


class MyRadiobutton:
    def __init__(self, text, value):
        Radiobutton(
            f_lef,
            text=text,
            value=value,
            #
            width=10,
            height=2,
            variable=r_var,
            command=change,
            indicatoron=0
        ).pack()


def change():
    if r_var.get() == 0:
        lab['text'] = "Василий"
    elif r_var.get() == 1:
        lab['text'] = "Пётр"
    elif r_var.get() == 2:
        lab['text'] = "Мария"


if __name__ == '__main__':
    root = Tk()

    f_lef = Frame(root)
    f_rig = Frame(root)

    r_var = IntVar()
    r_var.set(0)

    r1 = MyRadiobutton("Вася", 0)
    r2 = MyRadiobutton("Петя", 1)
    r3 = MyRadiobutton("Маша", 2)

    lab = Label(f_rig, width=40, bg="#f00")

    f_lef.pack(side=LEFT)
    f_rig.pack(side=RIGHT)
    lab.pack()

    root.mainloop()
