# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    def __init__(self, lenght, width, weight, area):
        # self.formula = (lenght, width)
        self.lenght = lenght
        self.width = width
        self.weight = weight
        self.area = area

    def formula(self):
        return self.lenght * self.width * self.weight * self.area / 1000


road = Road(20, 5000, 25, 5)
print(road.formula())



