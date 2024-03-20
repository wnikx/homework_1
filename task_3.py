class Server:
    """ Описание работы серверов в сети """

    ip_address: int = 1

    def __init__(self):
        """ Инициализация класса серверов """

        self.ip: int = Server.ip_address
        Server.ip_address += 1
        self.buffer: list = list()

    def send_data(self, data: Data):
        """ Функция для отправки пакетов из буфера """

        if self.get_ip() in Router.servers and data.ip in Router.servers:
            Router.buffer.append(data)

    def get_data(self) -> list:
        """ Возвращяет список принятых пакетов и очищает буфер """

        result = self.buffer
        self.buffer = list()
        return result

    def get_ip(self):
        """ Возвращает IP address """

        return self.ip


class Router:
    """ Описание работы роутеров в сети """

    servers: dict = {}
    buffer: list = list()

    def link(self, server: Server):
        """ Присоединение сервера  к роутеру """

        Router.servers[server.get_ip()] = server

    def unlink(self, server: Server):
        """ Отсоединение сервера от роутера """

        if server.get_ip() in Router.servers:
            del Router.servers[server.get_ip()]

    def send_data(self):
        """ Отправка всех пакетов из буфера роутера """

        for item in Router.buffer:
            Router.servers[item.ip].buffer.append(item.data)
        Router.buffer = list()


class Data:
    """ Описание пакета информации """

    def __init__(self, data, ip):
        """ Инициализация пакета """

        self.data: str = data
        self.ip: int = ip
