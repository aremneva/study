from tkinter import*
def change():
    if var.get()==0:
        label1['text']='1 килобайт = 2^10 байт'
    elif var.get() == 1:
        label1['text'] = '1 мегабайт =  2^20 байт'
    elif var.get() == 2:
        label1['text'] = '1 гигабайт = 2^30 байт'
    elif var.get() == 3:
        label1['text'] = '1 терабайт = 2^40 байт'

root=Tk()
var=IntVar()
var.set(0)
root.title("Выбор")
root.geometry("400x300")
root.configure(background='steelblue1')

rKb=Radiobutton(text="Кб",bg='red',variable=var, value=0)
rMb=Radiobutton(text="Мб",bg='salmon1', variable=var, value=1)
rGb=Radiobutton(text="Гб",bg='pink', variable=var, value=2)
rTb=Radiobutton(text="Тб",bg='plum1', variable=var, value=3)
label1=Label(text='Выберите единицу измерения',width=30,height=2,bg='light pink')
but=Button(text="Изменить",bg='azure', command=change)
rKb.pack()
rMb.pack()
rGb.pack()
rTb.pack()
but.pack()
label1.pack(side=BOTTOM)
root.mainloop()