import socket
import pickle


class Writer:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8004))

    def send_data(self, data):
        # Serialize the data object using pickle
        data_bytes = pickle.dumps(data)
        self.client_socket.sendall(data_bytes)
