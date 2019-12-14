import random
zn=random.randint(60,100)
l1=[random.randint(78,85) for i in range(1,100)]
s1=round(sum(l1)/len(l1))
l2=[random.randint(70,85) for i in range(1,100)]
s2=round(sum(l2)/len(l2))
def start(claim):
    print('Приём в ВУЗ открыт')
    print('Документы поданы')
    print('Проходной балл для 1 волны:',s1,' для 2 волны:',s2)
    claim['state']='analyze1'
def analyze1(claim):
    print('Результат вступительных испытаний:',zn)
    print('Конкурс 1 волна')
    if zn>s1:
        print('Попадание в 1 волну')
        claim['state']='treatment'
    else:
        claim['state']='analyze2'
def treatment(claim):
    print('Приказ о зачислении')
    claim['state']='end'
def analyze2(claim):
    print('Конкурс 2 волна')
    if zn>s2:
        print('Попадание во 2 волну')
        claim['state']='treatment'
    else:
        print('Конкурс не пройден')
        claim['state']='end'
def end(claim):
    print('Приём в ВУЗ закрыт')
    claim['state'] = None
state={'start':start,'analyze1':analyze1,'analyze2':analyze2,'treatment':treatment,'end':end}
def run():
    claim={'state':'start'}
    while claim['state'] is not None:
        fun=state[claim['state']]
        fun(claim)
run()