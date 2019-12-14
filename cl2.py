class Circle:
    def __init__(self,diameter):
         self.diameter=diameter
    def Circuit(self):
        return self.diameter * 3.14
    def Square(self):
        return ((self.diameter**2)/4 * 3.14)
C1=Circle(int(input("Введите диаметр первого круга:")))
C2=Circle(int(input("Введите диаметр второго круга:")))
print("Площадь первого круга равна:",C1.Square())
print("Длина окружности второго круга равна",C2.Circuit()," а площадь:",C2.Square())