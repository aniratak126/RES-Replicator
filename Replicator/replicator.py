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
    def send_to_reader(self):
        return 'TO DO'
        # Sent to the reader
        # Send the data to the appropriate Reader based on the dataset
        # dataset = input("Enter the dataset (A, B, C): ")
        # if dataset == 'A':
            # reader_a.receive_data(self.data)
        # elif dataset == 'B':
            # reader_b.receive_data(self.data)
        # elif dataset == 'C':
            # reader_c.receive_data(self.data)

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
        with connection:
            # Receive the data from the Writer component
            self.data = connection.recv(1024)

        # Forward the data to the Replicator component
        self.parent.send_data(self.data)

class ReplicatorReceiver:
    def __init__(self, parent):
        self.parent = parent
        self.data = None

    def receive_data(self, data):
        self.data = data
        data_obj = pickle.loads(self.data)
        print(f'Data successfully received: user id: {data_obj.id} consumption: {data_obj.consumption}')
        self.parent.send_to_reader(self.data)

if __name__ == '__main__':
    replicator = Replicator()
    replicator.run()