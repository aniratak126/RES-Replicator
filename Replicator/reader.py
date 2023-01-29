import socket
import pickle
from database import read_all_consumers, read_consumer, update_consumer, add_consumer

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
        print("3. Receive data.")
        try:
            option = int(input())    
        except:
            print("Option must be an integer")
            menu()

        if option == 1:
            read_all_cons()
        elif option == 2:
            read_one_cons()
        elif option == 3:
            return 0
        else:
            print("Invalid input, try again.")



class Reader:
    def __init__(self):
        self.data = None

    def receive_data(self, server_socket):
        # Accept an incoming connection from the Replicator component
        menu()
        while True:
            connection, address = server_socket.accept()
            with connection:
                # Receive the data from the Replicator component
                self.data = connection.recv(1024)

            data = pickle.loads(self.data)
            print(f'Data successfully received: user id: {data.id}')

            try:
                option = data.choice
            except:
                print("Option must be an integer")

            if option == 1:
                try:
                    if add_consumer(data.id, data.name, data.last_name, data.street, data.street_num, data.postal_code, data.city, 'consumers.db'):
                        print("Added successfully.")
                    else:
                        print('Consumer already exists.')
                except:
                    raise Exception()

            elif option == 2:
                print("Enter month of consumption: ")
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
            else:
                print('Invalid input.')
            menu()

    