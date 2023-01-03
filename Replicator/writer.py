import socket
import pickle

from data import Data


class Writer:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 8000))

    def send_data(self, user_id, consumption):
        # Serialize the data object using pickle
        data_bytes = pickle.dumps(Data(user_id, consumption))
        self.client_socket.sendall(data_bytes)

