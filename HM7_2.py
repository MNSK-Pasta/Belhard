from sqlalchemy import create_engine, Column, String, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///cars.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class BrandCar(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)

    name = Column(String)


class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)

    model = Column(String)
    release_year = Column(Integer)
    brand_car = Column(String, ForeignKey('brand.id'))
    rel = relationship('BrandCar', back_populates='cars')


BrandCar.cars = relationship(Car, order_by=Car.id, back_populates='rel')


def insertbrandcar():
    br1 = BrandCar(name=input('Введите марку машины '))
    session.add(br1)
    session.commit()
    cr1 = Car(model=input('Введите модель'), release_year=input('Введите год выпуска '),
              brand_car=input("Введите id бренда"))
    session.add(cr1)
    session.commit()


def selectbrand():
    br1 = session.query(BrandCar).all()
    for i in br1:
        print('name: ', i.name)


def selectcar():
    cr1 = session.query(Car).all()
    for c in cr1:
        print('model: ', c.model, 'year: ', c.release_year, 'id: ', c.brand_car)


def updatebrand():
    session.query(BrandCar).filter(BrandCar.id == input('Введите id бренда ')). \
        update({BrandCar.name: input('Введите новую марку ')}, synchronize_session=False)
    session.commit()


def updatecar():
    session.query(Car).filter(Car.id == input('Введите id машины ')). \
        update({Car.model: input('Введите новую модель '),
                Car.release_year: input('Введите новый год '),
                Car.brand_car: input('Введите новый id бренда ')}, synchronize_session=False)
    session.commit()


def deletebrand():
    session.query(BrandCar).filter(BrandCar.id == input('Введите id бренда ')).delete()
    session.commit()


def deletecar():
    session.query(Car).filter(Car.id == input('Введите id машины ')).delete()
    session.commit()


while True:
    ch = int(input(' Для вставки введите - 1 \n Для просмотра таблицы brand введите - 2 \n '
                   'Для просмотра таблицы cars введите - 3 \n Для обновления таблмцы brand введите - 4 \n'
                   ' Для обновления таблицы cars введите - 5 \n Для удаления по id из таблицы brand введите - 6\n'
                   ' Для удаления по id из таблицы cars введите - 7\n Для выхода введите - 0\n Ввод:'
                   ''))
    if ch == 0:
        break
    else:
        {1:insertbrandcar, 2:selectbrand, 3:selectcar, 4:updatebrand, 5:updatecar, 6:deletebrand, 7:deletecar}.get(ch)()