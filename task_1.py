class ObjList:
    """ Объект ObjList """

    def __init__(self, data: str):
        """ Инициализация объекта ObjList """

        self.__data: str = data
        self.__prev: str | None = None
        self.__next: str | None = None

    def get_data(self) -> str:
        """ Получение значение приватного свойства __data """

        return self.__data

    def set_data(self, value: str) -> None:
        """ Изменение приватного свойства __data на значение value """

        self.__data = value

    def get_next(self) -> str | None:
        """ Получение значение приватного свойства __next """

        return self.__next

    def set_next(self, value: str) -> None:
        """ Изменение приватного свойства __next на значение value """

        self.__next = value

    def get_prev(self) -> str | None:
        """ Получение значение приватного свойства __prev """

        return self.__prev

    def set_prev(self, value: str) -> None:
        """ Изменение приватного свойства __next на значение value """

        self.__prev = value

    data = property(get_data, set_data)
    next = property(get_next, set_next)
    prev = property(get_prev, set_prev)


class LinkedList:
    """ Класс представляет связный список """

    def __init__(self):
        """ Инициализация связного списка """

        self.head: None | ObjList = None
        self.tail: None | ObjList = None

    def add_obj(self, obj: ObjList) -> None:
        """ Добавление нового объекта obj класса ObjList в конец связнаго списка """

        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = obj
            obj.prev = current
            self.tail = current.next

    def remove_obj(self) -> None:
        """ Удаление последнего объекта из связного списка """

        last = self.tail
        if last:
            if last.prev:
                last.prev.next = None
            else:
                self.head = None
                self.tail = None

    def get_data(self) -> list:
        """ Получение списка из строк локального свойства __data всех объектов связного списка """

        result_lst = list()
        current = self.head
        while current:
            result_lst.append(current.data)
            current = current.next
        return result_lst
