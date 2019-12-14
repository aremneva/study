from tkinter import*
root=Tk()
root.geometry('200x335')
def Grey(): #Перекрашивает все кнопки в серый
    red['bg']='#f0f0f0'
    yel['bg']='#f0f0f0'
    grn['bg'] = '#f0f0f0'
def Yellow(): #Перекрашивает первую кнопку в желтый
    Grey()
    lbl['text']='Жди - желтый свет!'
    yel['bg']='yellow'
def Red():
    Grey()
    lbl['text']='Стой - красный свет!'
    red['bg']='red'
def Green():
    Grey()
    lbl['text']='Иди - зеленый свет!'
    grn['bg']='green'
lbl=Label(height=5)
lbl.pack(fill='both')
red=Button(text="Красный",bg='#f0f0f0',command=Red,height=5)
red.pack(fill='both')

yel=Button(text="Желтый",bg='#f0f0f0',command=Yellow,height=5)
yel.pack(fill='both')

grn=Button(text="Зеленый",bg='#f0f0f0', command=Green,height=5)
grn.pack(fill='both')
root.mainloop()