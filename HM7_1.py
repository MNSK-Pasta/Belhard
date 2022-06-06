from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

engine = create_engine('sqlite:///products.db', echo=True)
meta = MetaData()
conn = engine.connect()

products = Table(
    'products', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('price', Integer),
    Column('amount', Integer),
    Column('comment', String),
)


def inse():
    ins = products.insert().values(name=input('Введите имя '), price=input('Введите цену '),
                                   amount=input('Введите количество '), comment=input('Коммент '))
    conn.execute(ins)


def sele():
    sel = products.select()
    res = conn.execute(sel)
    for i in res:
        print(i)


def upde():
    upd = products.update().where(products.c.id == input('Введите id продукта ')).values(name=input('Введите имя '),
                                                                                         price=input('Введите цену '),
                                                                                         amount=input(
                                                                                             'Введите количество '),
                                                                                         comment=input('Коммент '))
    conn.execute(upd)


def delet():
    dele = products.delete().where(products.c.id == input('Введите id продукта '))
    conn.execute(dele)


while True:
    pri = int(input(
        ' Вставка продукта - 1 \n Обновление продукта - 2 \n Удаление продукта - 3 \n Просмотор таблицы - 4 \n Выход - 0 \n '))
    if pri == 0:
        break
    else:
        {1:inse, 2:upde, 3:delet, 4:sele}.get(pri)()