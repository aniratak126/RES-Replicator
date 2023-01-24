from writer import Writer

if __name__ == '__main__':
    writer = Writer()
    while True:
        user_id = input('Enter user id: ')
        consumption = input('Enter consumption: ')
        if consumption > 0 and user_id > 0:
            writer.send_data(user_id, consumption)
        else:
            print("Consumption and Id must be a positive number!")

