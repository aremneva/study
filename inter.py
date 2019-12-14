from tkinter import *
from tkinter import messagebox as mb
import random

_root = Tk()
_root.title("Камень-Ножницы-Бумага")
_root.geometry("800x550")
_root.configure(background='#FFC873')
choices = []  # Список,в котором хранятся ходы пользователя
n = 0  # Количество побед
wt = '#ffffff'  # белый цвет
f = ('Bookman Old Style', 12)  # шрифт
yell = PhotoImage(file='yell.png')
stone = PhotoImage(file='rock.png')
scs = PhotoImage(file='scs.png')
paper = PhotoImage(file='ppr.png')


def check():
    """
    Диалоговое окно при выходе из программы
    :return:
    """
    answer = mb.askyesno(title='Выход', message="Завершить процесс?")
    if answer == True:
        _root.destroy()


def count():  # заполнение списка с ходами пользователя
    choices.append(rez2['text'])


def Stat():  # Метод задания статистики в новом окне
    root1 = Tk()
    root1.geometry("500x200")
    root1.configure(background='#7080D7')
    root1.title('Статистика')
    var = IntVar()
    var.set(0)
    user1 = Radiobutton(root1, text='Пользователь 1', variable=var, value=0, bg='#EC6AA1', font=f)
    user1.grid(row=0, column=2)
    user2 = Radiobutton(root1, text='Пользователь 2', variable=var, value=1, bg='#EC6AA1', font=f)
    user2.grid(row=1, column=2)

    def Save():
        if var.get() == 0:
            stsF = open('user1.txt', 'w')  # открытие файла для записи
        elif var.get() == 1:
            stsF = open('user2.txt', 'w')
        print(var.get())
        stsF.write(L1 + '\n' + L2 + '\n' + L3 + '\n' + L4)  # запись в файл статистики
        stsF.close()

    L1 = 'Пользователь выйграл ' + str(n) + ' раз(а)'
    L2 = 'Выбрано "Камень" ' + str(choices.count('Камень')) + " раз(а)"
    L3 = 'Выбрано "Ножницы" ' + str(choices.count('Ножницы')) + " раз(а)"
    L4 = 'Выбрано "Бумага" ' + str(choices.count('Бумага')) + " раз(а)"
    save = Button(root1, text='Сохранить', width=10, height=2, bg='#A4F43D', command=Save, fg='#ffffff', font=f)
    save.grid(row=1, column=0, columnspan=2)

    # borderwidth-Граница для метки, highlightthickness- прямоугольник, который окружает весь виджет
    listbox1 = Listbox(root1, bg='#7080D7', height=6, font=f, width=30, fg=wt, borderwidth=0, highlightthickness=0)
    list1 = [L1, L2, L3, L4]
    for i in list1:  # Поочередно добавляет в listbox все элементы списка(Чтобы элементы были с новой строки)
        listbox1.insert(END, i)
    listbox1.grid(row=0, column=0)


def lose():  # Результат при проигрыше
    rez3['text'] = 'Проигрыш!'
    rez3['bg'] = '#FF7640'
    count()
    c = Canvas(_root, width=100, height=70, bg='#FF0000')
    c.create_line(20, 20, 90, 60, width=20, fill='white')
    c.create_line(90, 20, 20, 60, width=20, fill='white')
    c.grid(row=0, column=0, columnspan=2, rowspan=4)
    c.after(500, lambda: c.destroy())


def win():  # при выиграше
    global n
    n += 1
    rez3['text'] = 'Победа!'
    rez3['bg'] = '#7CE700'
    count()
    c = Canvas(_root, width=100, height=70, bg='#7CE700')
    c.create_line(30, 40, 50, 60, 80, 10, width=15, fill='white')
    c.grid(row=0, column=0, columnspan=2, rowspan=4)
    c.after(500, lambda: c.destroy())  # закрытие холста через 500 миллисекунд


def draw():  # при ничье
    rez3['text'] = 'Ничья'
    rez3['bg'] = '#FFC300'
    count()
    c = Canvas(_root, width=100, height=70, bg='#FFD300')
    c.create_line(30, 40, 80, 40, width=15, fill='white')
    c.grid(row=0, column=0, columnspan=2, rowspan=4)
    c.after(500, lambda: c.destroy())


def PC_Hod():  # Ход компьютера + определение результата раунда
    rsp = ['Камень', 'Ножницы', 'Бумага']
    PC = random.choice(rsp)
    rez1['text'] = PC
    if PC == rez2['text']:
        draw()
    if PC != rez2['text']:
        if rez2['text'] == rsp[0] and rez1['text'] == rsp[1]:
            win()
        elif rez2['text'] == rsp[1] and rez1['text'] == rsp[2]:
            win()
        elif rez2['text'] == rsp[2] and rez1['text'] == rsp[0]:
            win()
        else:
            lose()


def GameS():
    rez2['text'] = sc['text']
    PC_Hod()


def GameR():
    rez2['text'] = rc['text']
    PC_Hod()


def GameP():
    rez2['text'] = pr['text']
    PC_Hod()


# Фоновое изображенние
img = Label(image=yell, width=800, height=600)
img.grid(row=0, column=0, rowspan=5, columnspan=5)
# Кнопки Камень-Ножницы-Бумага
rc = Button(image=stone, text='Камень', background="gray", command=GameR)
rc.grid(row=0, column=2)
sc = Button(image=scs, text='Ножницы', background="lightcoral", command=GameS)
sc.grid(row=1, column=2)
pr = Button(image=paper, text='Бумага', background="bisque2", command=GameP)
pr.grid(row=2, column=2)
# Ходы
hod1 = Label(text='Ход Компьютера', width=30, height=2, bg='#FFCA00', fg=wt, font=f)
hod1.grid(row=0, column=0)
rez1 = Label(text='', width=30, height=5, bg='#409300', fg=wt, font=f)
rez1.grid(row=1, column=0)
hod2 = Label(text='Ход Пользователя', width=30, height=2, bg='#BFA130', fg=wt, font=f)
hod2.grid(row=0, column=1)
rez2 = Label(text='', width=30, height=5, bg='#1F7D63', fg=wt, font=f)
rez2.grid(row=1, column=1)
# Результат и Статистика
stat = Button(text='Статистика', width=15, height=3, bg='#343085', fg=wt, command=Stat, font=f)
stat.grid(row=3, column=0, columnspan=2)
rez3 = Label(text='', width=20, height=3, bg='#06799F', font=f, fg=wt)
rez3.grid(row=2, column=0, columnspan=2)
# Выход
exit = Button(text='Выход', width=15, height=3, bg='red', fg=wt, command=check, font=f)
exit.grid(row=3, column=2, columnspan=2)

_root.mainloop()
