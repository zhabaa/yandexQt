import requests
import sqlite3
from subfunc.NewsDataBase import NewsDataBase


class NewsParser:
    def __init__(self, token) -> None:
        self.token = token
        self.Ndb = NewsDataBase()

    def get_news(self) -> dict:
        """Получам новости"""

        try:
            response = requests.get(
                f"https://newsdata.io/api/1/news?apikey={self.token}&language=ru"
            )
        except Exception as ex:
            return ex

        data = response.json()
        result = dict()

        for news in data["results"]:
            result[news["article_id"]] = {
                "Заголовок": news["title"],
                "Ссылка": news["link"],
                "Дата": news["pubDate"],
            }

        for article, info in result.items():
            try:
                self.Ndb.add_news(
                    article=article,
                    title=info["Заголовок"],
                    date=info["Дата"],
                    link=info["Ссылка"],
                )
            except sqlite3.IntegrityError:
                pass

        self.Ndb.close()

        return result
