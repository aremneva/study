class Transport:
    def __init__(self,type,carrying):
        self.type = type
        self.carrying = carrying
    def Type_Carrying(self):
        self.type = str(input("Введите тип транспорта:"))
        if (self.type == "Машина"):
            self.carrying= 700
            print("Грузоподъемность равна:",self.carrying)
        elif (self.type == "Катер"):
            self.carrying= 900
            print("Грузоподъемность равна:", self.carrying)
        elif (self.type == "Мотоцикл"):
            self.carrying = 200
            print("Грузоподъемность равна:", self.carrying)

class Automobile(Transport):
    def __init__(self,weight):
        self.weight = weight
    def Type_Carrying(self):
        super().Type_Carrying()
    def weight_cargo(self):
        if self.weight < self.carrying:
            while self.weight < self.carrying:
                point = (input("Увеличить вес груза?:"))
                if point == "Да":
                    self.weight += 10
                    print("Текущий вес:",self.weight)
                elif point == "Нет":
                    print("Итоговый вес: ",self.weight)
                    break
                else:
                    print("Неизвестный ответ.")
                    break
        if self.weight > self.carrying:
            print("Превышение максимального веса груза!")
        if self.weight == self.carrying:
            print("Максимальный вес груза!")
#car1=Automobile(int(input("Введите вес груза:")))
#car1.Type_Carrying()
#car1.weight_cargo()
#bike=Automobile(int(input("Введите вес груза:")))
#bike.Type_Carrying()
#bike.weight_cargo()
boat=Automobile(200)
print(boat.weight)