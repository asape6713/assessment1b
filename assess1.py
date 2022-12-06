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
def insert_contacts(C, id, first_name, last_name, title, organization):
    cur = C.cursor()
    cur.execute(f"INSERT INTO contacts (id, first_name, last_name, title, organization) VALUES ('{id}','{first_name}', '{last_name}','{title}'.'{organization}');")
    cur.close()
    #delets contact from table
def delete_contacts(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM contacts WHERE id = '{id}';")
    cur.close()
def save_contacts(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_contacts(conn))
    elif cmd == "insert": # insert 
        id = input("  id: ")
        first_name = input("  firstname: ")
        last_name = input("  last_name: ")
        title= input("  title: ")
        organization = input("  organization: ")
        insert_contacts(conn, id, first_name, last_name, title, organization)
    elif cmd == "delete":
        id= input("  id: ")
        delete_contacts(conn, ID)
    elif cmd == "quit":
        save_contacts(conn)
        exit()