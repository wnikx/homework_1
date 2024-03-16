import random


class Cell:
    def __init__(self, mine=False, arround_mines=0):
        self.arround_mines = arround_mines
        self.mine = mine
        self.fl_open = False

    def __repr__(self):
        if self.fl_open:
            if self.mine:
                return " * "
            return f" {self.arround_mines} "
        return " # "


class GamePole:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pole = self.create_board()
        self.init()

    def create_board(self):
        """ Создаем поле """

        return [[Cell() for i in range(self.n)] for j in range(self.n)]

    def init(self):
        """ Инициализация поля """

        mines = self.mines_place()
        for row, col in mines:
            self.pole[row][col].mine = True
            self.update_arround_mines(
                row, col)

    def mines_place(self):
        """ Выбираем случайные координаты для мин """

        result = []
        for i in random.sample(range(0, self.n ** 2), self.m):
            if i < 10:
                result.append((0, i))
            else:
                place = str(i)
                result.append((int(place[0]), int(place[1])))
        return result

    def update_arround_mines(self, row, col):
        """ Вычисляем кол-во мин по соседству """

        directions = [(i, j) for i in range(-1, 2)
                      for j in range(-1, 2) if (i != 0 or j != 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.n and 0 <= new_col < self.n:
                self.pole[new_row][new_col].arround_mines += 1

    def show(self):
        """ Демонстрация поля """

        for i in self.pole:
            print(*i)

    def open_cage(self, cor_1, cor_2):
        """ Функция открывает клетку """

        self.pole[cor_1][cor_2].fl_open = True


# pole_game = GamePole(10, 12)
# pole_game.open_cage(1, 3)
# pole_game.open_cage(2, 3)
# pole_game.open_cage(3, 3)
# pole_game.open_cage(4, 3)
# pole_game.open_cage(5, 3)
# pole_game.open_cage(6, 3)
# pole_game.show()
# Чтобы открыть все клетки удали 11 и 15 строчку и выровняй по синтаксису :)
