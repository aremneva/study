class Worker:
    def __init__(selfself,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)
    def Pers_NDFL(self):
        return self.pay*0.13
bob=Worker('Bob Smith',50000)
sue=Worker('Sue Jones',60000)
