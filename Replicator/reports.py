import sqlite3
from collections import defaultdict

def monthly_consumption_by_street(street, db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # izvucemo sve potrosace iz jedne ulice
    statement1 = "SELECT id FROM consumers WHERE street = ?"
    cur.execute(statement1,(street,))

    data = cur.fetchall()
    if not data:
        conn.close()
        print(f"Street '{street}' does not exists!")
        return 0, 0
    
    # za svaki mesec izvucemo potrosnju za zadatu ulicu po potrosacu
    cur.execute("SELECT consumption, month FROM consumption_info WHERE consumer_id IN (SELECT id FROM consumers WHERE street = ?)",(street,))
    res = cur.fetchall()
    sum = defaultdict(int)

    # za svakog potrosaca jos saberemo potrosnju po mesecu
    for cons, month in res:
        sum[month] += cons

    return street, sum
    conn.close()

def monthly_consumption_by_consumer(id, db_name = 'consumers.db'):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # zbog provere da li id postoji
    cur.execute("""SELECT id FROM consumers WHERE id = ?""", (id,))
    data = cur.fetchall()

    if not data:
        conn.close()
        print("Consumer does not exists!")
        return 0, 0

    # ako postoji izvuci potrosnju po mesecu
    cur.execute("SELECT consumption, month FROM consumption_info WHERE consumer_id = ?",(id,))
    res = cur.fetchall()
    sum = defaultdict(int)

    # visak jer se ovo odvija u database.update_consumer
    for cons, month in res:
        sum[month] += cons
    
    conn.close()
    return id, sum

def menu():
    while True:
        print('******* Reports *******')
        print('1 - Monthly water consumption by street')
        print('2 - Monthly water consumption by consumer')
        print('Press 0 to exit')

        try:
            option = int(input())
        except:
            print("Inserted value is not an integer!")
            return 0

        if option == 1:
            print("Insert street name:")
            street = input()
            result = monthly_consumption_by_street(street)

            if result != (0,0):
                print('*** Mesecna potrosnja ***')
                print(f"ULICA - {result[0]}")
                for key, value in sorted( result[1].items()):
                    print(f"Mesec:{key}  Potrosnja:{value}")
                    
        elif option == 2:
            print('Insert consumer ID:')
            try:
                id = int(input())
            except:
                print('Inserted id is not an integer')
                return 0
            result = monthly_consumption_by_consumer(id)
            if result != (0,0):
                print('*** Mesecna potrosnja ***')
                print(f"Consumer ID - {result[0]}")
                for key, value in sorted( result[1].items()):
                    print(f"Mesec:{key}  Potrosnja:{value}")

        elif option == 0:
            return 0

        else:
            print('Invalid input')
            return 0

if __name__ == "__main__":
    menu()