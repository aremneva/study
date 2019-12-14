from tkinter import*
def exitwin(event): #метод завершения mainloop
    root.destroy()
def inLabel(event): #отображения текста на Label
    t=ent.get(); lbl.configure(text=t)
def selectAll(event):#задает время через какое будет выведена данная функция
    root.after(10,select_all,event.widget)
def select_all(widget):#Выделение всех вводимых символов
    widget.selection_range(0,END)
    widget.icursor(END)#курсор в конец
root=Tk()
ent=Entry(width=40); ent.focus_set(); ent.pack()
lbl=Label(height=3, fg='orange',bg='darkgreen',font='Verdana 24')
lbl.pack(fill=X)
ent.bind('<Return>',inLabel)#Возвращение значения
ent.bind('<Control-a>',selectAll)#выполнение метода по нажатию Control-q
root.bind('<Control-q>',exitwin)#выполнение метода по нажатию Control-q
root.mainloop()