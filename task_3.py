class Server:
    ip_address = 1

    def __init__(self):
        self.ip = Server.ip_address
        Server.ip_address += 1
        self.buffer = list()

    def send_data(self, data):
        if self.get_ip() in Router.servers and data.ip in Router.servers:
            Router.buffer.append(data)

    def get_data(self):
        result = self.buffer
        self.buffer = list()
        return result

    def get_ip(self):
        return self.ip


class Router:
    servers = {}
    buffer = list()

    def link(self, server: Server):
        Router.servers[server.get_ip()] = server

    def unlink(self, server: Server):
        if server.get_ip() in Router.servers:
            del Router.servers[server.get_ip()]

    def send_data(self):
        for item in Router.buffer:
            Router.servers[item.ip].buffer.append(item.data)
        Router.buffer = list()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
