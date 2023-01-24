import socket
import pickle


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
        self.server_socket.bind(('localhost', 8004))
        self.server_socket.listen()

    def receive_data(self):
        # Accept an incoming connection from the Writer component
        connection, address = self.server_socket.accept()
        with connection:
            # Receive the data from the Writer component
            self.data = connection.recv(1024)

        # Forward the data to the Replicator component
        self.parent.send_data(self.data)


class ReplicatorReceiver:
    def __init__(self, parent):
        self.parent = parent
        self.data = None

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_data(self, data):
        self.data = data
        data_obj = pickle.loads(self.data)
        print(f'Data successfully received: user id: {data_obj.id}')
        self.send_to_reader(self.data)

    def send_to_reader(self, data):

        # Send to the reader
        # Send the data to the appropriate Reader based on the dataset
        dataset = input("Enter the reader (A, B, C): ")
        if dataset == 'A':
            self.client_socket.connect(('localhost', 6001))
            self.client_socket.sendall(self.data)
        elif dataset == 'B':
            self.client_socket.connect(('localhost', 6002))
            self.client_socket.sendall(self.data)
        elif dataset == 'C':
            self.client_socket.connect(('localhost', 6003))
            self.client_socket.sendall(self.data)


if __name__ == '__main__':
    replicator = Replicator()
    replicator.run()