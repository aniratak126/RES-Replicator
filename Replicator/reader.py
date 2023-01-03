import socket
import pickle
from database import read_all_consumers, read_consumer, update_consumer

def read_all_cons(db_name = 'consumers.db'):
    print("******* All Consumers *******")
    info = read_all_consumers(db_name)
    print(str(info))

def read_one_cons(db_name = 'consumers.db'):
    print("Enter ID of Consumer: ")
    try:
        id = int(input())    
    except:
        print("Value is not an integer")
        return 0
    
    print("******* Consumer *******")
    info = read_consumer(id, db_name)
    print(str(info))

def menu():
    while True:
        print("******* Enter Option *******")
        print("1. List All Consumers.")
        print("2. List One Consumer by ID.")
        print("Press 0 to exit.")
        try:
            option = int(input())    
        except:
            print("Option must be an integer")
            return 0

        if option == 1:
            read_all_cons()
        elif option == 2:
            read_one_cons()
        elif option == 0:
            return 0
        else:
            print("Invalid input, try again.")


class Reader:
    def run(self):
        self.receive_data()

    def __init__(self):
        self.data = None

        # Create a server socket to listen for incoming connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 8001))
        self.server_socket.listen()

    def receive_data(self):
        # Accept an incoming connection from the Replicator component
        while True:

            connection, address = self.server_socket.accept()
            with connection:
                # Receive the data from the Replicator component
                self.data = connection.recv(1024)

            data = pickle.loads(self.data)
            print(f'Data successfully received: user id: {data.id} consumption: {data.consumption}')

            print("Enter moth of consumption: ")
            try:
                month = int(input())
            except:
                print("Input must be an integer")
                return 0

            if month < 1 or month > 12:
                print("Invalid input")
                return 0

            try:
                update_consumer(data.id, data.consumption, month)
            except: 
                raise Exception()            

        
if __name__ == '__main__':
    menu()
    reader = Reader()
    reader.run()
    
    