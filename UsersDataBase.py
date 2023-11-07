import sqlite3


class DataBase:
    def __init__(self):
        self.connect = sqlite3.connect("users1.db")
        self.cursor = self.connect.cursor()

    def add_user(self, login, password):
        self.cursor.execute(
            "INSERT INTO users (login, password) VALUES (?, ?)", (login, password)
        )

    def get_info(self):
        data = self.cursor.execute(
            "SELECT login, password from users"
        )
        return dict(data.fetchall())

    def close(self):
        self.connect.commit()
        self.connect.close()
