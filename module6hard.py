
class Figure:
    sides_count = 0
    filled = bool

    def __init__(self, color, *sides):
        if all(0 <= i <= 255 for i in color) and len(color) == 3:
            self.__color = list(color)
        else:
            self.__color = (0, 0, 0)
        self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        new_sides = list(sides)
        if self.sides_count == 12 and all(i > 0 for i in new_sides):
            if len(new_sides) == 1:
                return True
            elif len(new_sides) == 12:
                new_sides = set(new_sides)
                return len(new_sides) == 1
            else:
                False
        if self.sides_count == 3 and len(new_sides) == 3 and all(i > 0 for i in new_sides):
            m = max(new_sides)
            new_sides.remove(m)
            return m <= sum(new_sides)
        return self.sides_count == len(sides) and all(i > 0 for i in sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if self.sides_count == 12 and len(new_sides) == 1:
                self.__sides = list(new_sides) * 12
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        super().__init__(color, *sides)
        __radius = sides[0] / (2 * 3.14)
        self.__radius = __radius

    def get_square(self):
        new_radius = self._Figure__sides[0] / (2 * 3.14)
        self.__radius = new_radius
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        sides_ = list(sides)
        m = max(sides_)
        sides_.remove(m)
        if m >= sum(sides_) or len(sides) != 3:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)
        p = sum(sides) / 2
        self.__height = (p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])) ** 0.5 * 2 / sides[0]

    def get_square(self):
        p = sum(self._Figure__sides) / 2
        self.__height = ((p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) *
                          (p - self._Figure__sides[2])) ** 0.5 * 2 / self._Figure__sides[0])
        return self._Figure__sides[0] * self.__height / 2


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1]
        sides = list(sides) * 12
        super().__init__(color, *sides)

    def get_volume(self):
        return (self._Figure__sides[0]) ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
