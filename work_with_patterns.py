import random
zn=random.randint(60,100)
zn1=80
zn2=70
def start(claim):
    print('Приём в ВУЗ открыт')
    print('Документы поданы')
    print('Проходной балл для 1 волны:',zn1,' для 2 волны:',zn2)
    claim['state']='analyze1'
def analyze1(claim):
    print('Результат вступительных испытаний:',zn)
    print('Конкурс 1 волна')
    if zn>zn1:
        print('Попадание в 1 волну')
        claim['state']='treatment'
    else:
        claim['state']='analyze2'
def treatment(claim):
    print('Приказ о зачислении')
    claim['state']='end'
def analyze2(claim):
    print('Конкурс 2 волна')
    if zn>zn2:
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