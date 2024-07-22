class Figure:
    sides_count = 0

    def __init__(self, __color, __sides, filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return [*self.__color]

    def __is_valid_color(self, r, g, b):
        if not all(isinstance(i, int) for i in (r, g, b)):
            return False
        if not all(0 <= i <= 255 for i in (r, g, b)):
            return False

        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, *sides):
        sides = []
        if not all(isinstance(side, int) for side in sides) and all(side > 0 for side in sides):
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled=True, __radius=0):
        super().__init__(__color, __sides, filled)
        if len(__sides) != self.sides_count:
            self.__sides = 1
        self.__radius = __sides[0] / 2 * 3.1415

    def get_square(self):
        return (self.__radius ** 2) * 3.1415


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__height = [self.sides_count ** 0.5 / 2 * i for i in self.get_sides()]

    def get_height(self, side=0):
        return self.__height[side]

    def get_square(self):
        return self.get_height() * self.get_sides()[0] / 2


class Figure:
    sides_count = 0

    def __init__(self, color, *side, filled=True):
        self.__sides = [*side]
        self.__color = [*color]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if not all(isinstance(i, int) for i in (r, g, b)):
            return False
        if not all(0 <= i <= 255 for i in (r, g, b)):
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        sides = []
        if not all(isinstance(side, int) for side in sides) and all(side > 0 for side in sides):
            return False
        return True

    def get_sides(self):
        if len(self.__sides) == 1:
            return [*self.__sides] * self.sides_count

    def __len__(self):
        return sum(self.get_sides())

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides) and len(self.__sides) == self.sides_count:
            self.__sides = sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *side):
        super().__init__(color, *side)
        self.__radius = self.get_sides()[0] // 2

    def get_square(self):
        return (self.__radius ** 2) * 3.1415


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            sides = sides * self.sides_count


    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


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

