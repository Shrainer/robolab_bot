import sqlite3

class database():
    def __init__(self):
        self("""CREATE TABLE IF NOT EXISTS UsersZXC
            (user_id integer, user_name text, level integer)"""
            )
        self("""CREATE TABLE IF NOT EXISTS MediaZXC
            (media_name text, media_path text, media_type text)"""
            )

    def __call__(self, command):
        with sqlite3.connect("mydatabase.db") as self._conn:
            self._cursor = self._conn.cursor()
            result = self._cursor.execute(command)
            self._conn.commit()
            return result

    """
    def create(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS UsersZXC
                    (user_id integer, user_name text, level integer)
                    ")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS MediaZXC
                    (media_name text, media_path text, media_type text)
                    ")
        self._conn.commit()


    def add_user(self, id, name, level):
        self._cursor.execute(f"INSERT INTO UsersZXC (user_id, user_name, level)
                      VALUES ({id}, '{name}', {level}
                      )")
        self._conn.commit()


    def delete_user(self, name):
        self._cursor.execute(f"DELETE FROM UsersZXC WHERE user_name = '{name}'")
        self._conn.commit()


    def add_media(self, name, path, type):
        self._cursor.execute(f"INSERT INTO MediaZXC (media_name, media_path, media_type)
                      VALUES ('{name}', '{path}', '{type}'
                      )")
        self._conn.commit()


    def select(self, table, *args):
        if not(args):
            for i in self._cursor.execute(f"SELECT * FROM {table}"):
                yield i
        else:
            if(len(args) == 1):
                for i in self._cursor.execute(f"SELECT {args[0]} FROM {table}"):
                    yield i[0]
            else:
                for i in self._cursor.execute(f"SELECT * FROM {table} WHERE {args[0]} = '{args[1]}'"):
                    yield i
    """

if __name__ == '__main__':
    data = database()
    r = data("select", "UsersZXC")
    print(list(r))

#todo:
#сохранять информацию пользователя в словарь
#запихнуть всё в один универсальный __call__
#сделать оболочку для уровней доступа
