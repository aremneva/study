from tkinter import*
root=Tk()

users=[['Anne','pswd1'],['Peter','pswd2'],['Chris','pswd1']]


for x in range(len(users)):
    l=Checkbutton(root,text=users[x][0],variable=users[x])
    print('l=Checkbutton(root,text= '+\
    str(users[x][0])+',variable='+str(users[x]))
    l.pack(anchor='w')
    users[x].select(1)

root.mainloop()