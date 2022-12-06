import psycopg2
from psycopg2 import *
conn = psycopg2.connect(
   host="localhost",
   port=5432,
   database="assessmentdb.sql",
   user="postgres",
   password="Vera1234?"
)

def read_contacts(C):
    cur = C.cursor()
    cur.execute("SELECT id, first_name, last_name, title, organization;")
    rows = cur.fetchall()
    cur.close()
    return rows
def insert_contacts(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        insert_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()