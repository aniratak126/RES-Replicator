from writer import Writer
from data import Data, NewUser
if __name__ == '__main__':
    writer = Writer()
    while True:
        print("******* Enter Option *******")
        print("1. Add new user.")
        print("2. Add consumption.")
        try:
            option = int(input())
        except:
            print("Option must be an integer")

        if option == 1:
            try:
                id = int(input('Enter user id:'))
                if id <= 0:
                    print('Id must be a positive number.')
                    id = int(input('Enter user id:'))
                name= input('Enter name:')
                last_name = input('Enter last name:')
                street = input('Enter street:')
                street_num = int(input('Enter street number:'))
                if street_num < 0:
                    print("Street number must be a positive number.")
                    street_num = int(input('Enter street number:'))
                postal_code = int(input('Enter postal code'))
                if postal_code<0:
                    print("Postal code must be a positive number.")
                    postal_code = int(input('Enter postal code'))
                city = input('Enter city')
            except:
                print('Invalid input.')

            data = NewUser(id, name, last_name, street, street_num, postal_code, city)
            writer.send_data(data)

        elif option == 2:
            try:
                user_id = int(input('Enter user id: '))
                consumption = int(input('Enter consumption: '))
            except:
                print("Invalid input.")
            if consumption > 0 and user_id > 0:
                data = Data(user_id, consumption)
                writer.send_data(data)
            else:
                print("Consumption and Id must be a positive number!")
        else:
            print('Invalid input.')
