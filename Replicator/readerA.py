from reader import Reader, menu
import socket


class ReaderA(Reader):
    def __init__(self):
        super().__init__()
        self.data = None
        # Create a server socket to listen for incoming connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8006))

    def run(self):
        self.server_socket.listen()
        self.receive_data(self.server_socket)

    def receive_data(self, server_socket):
        super().receive_data(server_socket=self.server_socket)
        self.data = super().data
        print('Reader A done.')


if __name__ == '__main__':
    readerA = ReaderA()
    menu()
    readerA.run()