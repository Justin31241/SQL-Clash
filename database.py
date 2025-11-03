import sqlite3

def get_connection(database):
    try:
        return sqlite3.connect(database)
    except Exception as e:
        print(f"Error: {e}!")
        raise

def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS cards (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        elixir INTEGER,
        damage INTEGER,
        health INTEGER
    )
    """
    try:
        with connection:
            connection.execute(query)
        print("Table created!")
    except Exception as e:
        print(e)

def add_card(connection, name:str, elixir:int, damage:int, health:int):
    query = "INSERT INTO cards (name, elixir, damage, health) VALUES (?, ?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, elixir, damage, health))
        print(f"Card: {name} was added to the database!")
    except Exception as e:
        print(e)

def fetch_cards(connection, condition: str = None) -> list[tuple]:
    query = "SELECT * FROM cards"


    if condition:
        query += f" WHERE {condition}"
    
    try:
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)


def drop_card(connection, card_id):
    query = f"DELETE FROM cards WHERE id= ?"

    try:
        with connection:
            connection.execute(query,(card_id))
        print(f"USER ID: {card_id} was deleted!")

    except Exception as e:
        print(e)

def main():
    connection = get_connection("clash.db")
    pulling = True

    try:
        
        create_table(connection)

        while pulling == True:
            start = input("Enter Option (Add, Delete, Update, Search, End)").lower()
            if start == 'add':
                name = input("Enter Name: ")
                elixir = int(input("Enter Elixir: "))
                damage = int(input("Enter Damage: "))
                health = int(input("Enter Health: "))
                add_card(connection, name, elixir, damage, health)
            elif start == 'search':
                for card in fetch_cards(connection):
                    print(card)
            elif start == 'delete':
                card = input("Card ID:")
                drop_card(connection, card)
            elif start == 'end':
                pulling = False
                print("Session Ended")

    finally:
        connection.close()
if __name__ == "__main__":
    main()
