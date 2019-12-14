import random
m1=["Кровать","Стол","Диван","Шкаф","Кресло","Тумба","Стул","Дверь"]
t1=["Компьютер","Телефон","Холодильник","Чайник","Пылесос","Микроволновка","Плита"]
e1=["Яблоко","Рис","Хлеб","Каша","Курица","Молоко"]
m="Мебель"
t="Техника"
e="Продукты"
money=[]
month=["Январь","Февраль","Апрель","Март","Май","Июнь"]
class Sale:
        def __init__(self,kind,sum):
                self.kind=kind
                self.sum=sum
                for j in range(6):
                    print("Введите сумму продаж за", month[j], "месяц:")
                    s1 = int(input(""))
                    money.append(s1)
        def Kind_of_product(self):
                print(self.kind,"Принадлежит к:")
                if self.kind in m1:
                        print(m)
                if self.kind in e1:
                        print(e)
                if self.kind  in t1:
                        print(t)
        def Sum(self):
            for j in range(6):
                print(month[j], ":", money[j])

        def Best_Month(self):
            mon=''
            max = 0
            for i in range(6):
                if money[i]>max:
                    max=money[i]
                    mon=month[i]
            print("Самый удачный месяц:",mon, max)
Item=Sale(input("Введите товар:"), money)
Item.Kind_of_product()
Item.Sum()
Item.Best_Month()