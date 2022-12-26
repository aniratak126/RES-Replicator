from writer import Writer

if __name__ == '__main__':
    user_id = input('Enter user id: ')
    consumption = input('Enter consumption: ')
    writer = Writer()
    writer.send_data(user_id, consumption)

