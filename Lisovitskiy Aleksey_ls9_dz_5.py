# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
# «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def draw(self):
        return 'Запуск отрисовки'

a = Stationery()
print(a.draw())

class Pen(Stationery):
    def draw(self):
        return 'Рисуем ручкой'

b = Pen()
print(b.draw())

class Pencil(Pen):
    def draw(self):
        return 'Рисуем карандашом'

c = Pencil()
print(c.draw())

class Handmaker(Pencil):
    def draw(self):
        return 'Маркер'

d = Handmaker()
print(d.draw())