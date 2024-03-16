class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, value):
        self.__data = value

    def get_next(self):
        return self.__next

    def set_next(self, value):
        self.__next = value

    def get_prev(self):
        return self.__prev

    def set_prev(self, value):
        self.__prev = value

    data = property(get_data, set_data)
    next = property(get_next, set_next)
    prev = property(get_prev, set_prev)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
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

    def remove_obj(self):
        last = self.tail
        if last:
            if last.prev:
                last.prev.next = None
            else:
                self.head = None
                self.tail = None

    def get_data(self):
        result_lst = list()
        current = self.head
        while current:
            result_lst.append(current.data)
            current = current.next
        return result_lst
