#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Напишите программу, состоящую из однострочного и многострочного
текстовых полей и двух кнопок "Открыть" и "Сохранить".
При клике на первую должен открываться на чтение файл, чье имя указано в
поле класса Entry, а содержимое файла должно загружаться в поле типа Text.
При клике на вторую кнопку текст, введенный пользователем в экземпляр Text,
должен сохраняться в файле под именем, которое пользователь указал в
однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта,
если указывать имена файлов без адреса.
"""
from tkinter import *


def load():
    file_name = ent.get()
    with open(file_name, 'r', encoding="utf-8") as f:
        txt.delete("1.0", END)
        txt.insert("1.0", f.read())


def save():
    file_name = ent.get()
    text = txt.get("1.0", END)
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(text)


if __name__ == '__main__':
    root = Tk()

    f_top = Frame(root)
    f_bot = Frame(root)

    ent = Entry(f_top, width=30)
    but1 = Button(f_top, text="Открыть", command=load)
    but2 = Button(f_top, text="Сохранить", command=save)

    txt = Text(f_bot, width=40, height=18, wrap="none")
    scroll_y = Scrollbar(f_bot, command=txt.yview)
    scroll_x = Scrollbar(f_bot, command=txt.xview, orient=HORIZONTAL)
    txt.config(
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    f_top.pack(padx=7, pady=3)
    f_bot.pack()
    ent.pack(side=LEFT)
    but1.pack(side=LEFT)
    but2.pack(side=LEFT)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=LEFT, fill=Y)
    txt.pack(side=LEFT)
    root.mainloop()
