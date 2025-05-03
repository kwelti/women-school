import sqlite3


def create_table():
    conn = sqlite3.connect("data_base.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS stravy (
         id INTEGER PRIMARY KEY,
         request TEXT)''')
    
def fill_quiz(path_to_db):
    n = int(input("Введіть кількість тем: "))
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    for i in range(n):
        name = input(f"Тема під номером {i}: ")
        cur.execute('''INSERT INTO quiz (name) VALUES (?)''', [name])
        conn.commit()
    conn.close()

    
    conn.commit()
    conn.close()