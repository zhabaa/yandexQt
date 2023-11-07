import sqlite3


class NewsDataBase:
    def __init__(self):
        self.connect = sqlite3.connect("D:/python/notifier/subfunc/news_db.db")
        self.cursor = self.connect.cursor()

    def add_news(self, article: str, title: str, date: str, link: str):
        self.cursor.execute(
            "INSERT INTO news (article, title, date, link) VALUES (?, ?, ?, ?)", (article, title, date, link)
        )

    def get_article(self):
        data = self.cursor.execute(
            "SELECT article from news"
        )
        return list(article[0] for article in data.fetchall())
    
    def get_info(self):
        data = self.cursor.execute(
            "SELECT article, title, date, link from news"
        )
        return dict(data.fetchall())

    def close(self):
        self.connect.commit()
        self.connect.close()
