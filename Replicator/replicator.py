import random
import socket
import pickle
import threading

class Replicator:
    def __init__(self):
        # Create the sender and receiver components
        self.sender = ReplicatorSender(self)
        self.receiver = ReplicatorReceiver(self)

    def run(self):
        # Set up the ReplicatorSender to receive data from the Writer component
        self.sender.receive_data()

    def send_data(self, data):
        # Forward the data to the ReplicatorReceiver
        self.receiver.receive_data(data)


class ReplicatorSender:
    def __init__(self, parent):
        self.parent = parent
        self.data = None

        # Create a server socket to listen for incoming connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8000))
        self.server_socket.listen()

    def receive_data(self):
        # Accept an incoming connection from the Writer component
        connection, address = self.server_socket.accept()
        #while True:
        with connection:
            while True:
                self.data = connection.recv(1024)
                if not self.data:
                    continue
                self.parent.send_data(self.data)


class ReplicatorReceiver:
    def __init__(self, parent):
        self.parent = parent
        self.data = None

        self.client_socketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socketA.connect(('localhost', 6001))
        self.client_socketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socketB.connect(('localhost', 6002))
        self.client_socketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socketC.connect(('localhost', 6003))

    def receive_data(self, data):
        self.data = data
        data_obj = pickle.loads(self.data)
        print(f'Data successfully received: user id: {data_obj.id}')
        self.send_to_reader(self.data)

    def send_to_reader(self, data):

        # Send to the reader
        # Send the data to the appropriate Reader based on the dataset
        list = ["A", "B", "C"]
        dataset = random.choice(list)
        if dataset == 'A':
            self.client_socketA.sendall(self.data)
        elif dataset == 'B':
            self.client_socketB.sendall(self.data)
        elif dataset == 'C':
            self.client_socketC.sendall(self.data)


if __name__ == '__main__':
    replicator = Replicator()
    replicator.run()