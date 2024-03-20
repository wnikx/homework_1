import random


class Cell:
    """ Класс для предстваления клетки игрового поля """

    def __init__(self, mine: bool = False, arround_mines: int = 0):
        """ Инициализация клетки для игрового поля """

        self.arround_mines: int = arround_mines
        self.mine: bool = mine
        self.fl_open: bool = False

    def __repr__(self):
        """ Отображение на игровом поле """

        if self.fl_open:
            if self.mine:
                return " * "
            return f" {self.arround_mines} "
        return " # "


class GamePole:
    """ Класс для управления игровым полем """

    def __init__(self, n: int, m: int):
        """ Инициализация игрового поля """

        self.n = n
        self.m = m
        self._pole = self.create_board()
        self.init()

    def create_board(self) -> list:
        """ Создаем поле """

        return [[Cell() for i in range(self.n)] for j in range(self.n)]

    def init(self):
        """ Инициализация поля """

        mines = self._mines_place()
        for row, col in mines:
            self._pole[row][col].mine = True
            self._update_arround_mines(
                row, col)

    def _mines_place(self) -> list:
        """ Выбираем случайные координаты для мин """

        result = []
        for i in random.sample(range(0, self.n ** 2), self.m):
            if i < 10:
                result.append((0, i))
            else:
                place = str(i)
                result.append((int(place[0]), int(place[1])))
        return result

    def _update_arround_mines(self, row: int, col: int):
        """ Вычисляем кол-во мин по соседству """

        directions = [(i, j) for i in range(-1, 2)
                      for j in range(-1, 2) if (i != 0 or j != 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.n and 0 <= new_col < self.n:
                self._pole[new_row][new_col].arround_mines += 1

    def show(self):
        """ Демонстрация поля """

        for i in self._pole:
            print(*i)

    def open_cage(self, cor_1: int, cor_2: int):
        """ Функция открывает клетку """

        self._pole[cor_1][cor_2].fl_open = True


# pole_game = GamePole(10, 12)
# pole_game.open_cage(1, 3)
# pole_game.open_cage(2, 3)
# pole_game.open_cage(3, 3)
# pole_game.open_cage(4, 3)
# pole_game.open_cage(5, 3)
# pole_game.open_cage(6, 3)
# pole_game.show()
# # Чтобы открыть все клетки удали 11 и 15 строчку и выровняй по синтаксису :)
