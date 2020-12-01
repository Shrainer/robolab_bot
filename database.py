import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


def create():
    cursor.execute("""CREATE TABLE UsersZXC
                (user_id integer, user_name text, level integer)
                """)
    cursor.execute("""CREATE TABLE MediaZXC
                (media_name text, media_url text)
                """)
    conn.commit()

def add_user(id, name, level):
    cursor.execute(f"""INSERT INTO UsersZXC (user_id, user_name, level)
                  VALUES ({id}, '{name}', {level}
                  )""")
    conn.commit()

def add_media(name, url):
    cursor.execute(f"""INSERT INTO MediaZXC (media_name, media_url)
                  VALUES ({name}, '{url}'
                  )""")
    conn.commit()

def select(table):
    for i in cursor.execute(f"SELECT * FROM {table}"):
        yield i

create()
