from plyer import notification as ntf
from subfunc.NewsDataBase import NewsDataBase as ndb


class ShowNotify:
    def __init__(self) -> None:
        self.news_db = ndb()

    def show_notify(self, kind: str, data: dict) -> None:
        """Показывает уведомление"""

        if kind == 'rate':
            usd = data['USD']
            eur = data['EUR']

            ntf.notify(
                title='Курс на данный момент',
                message=f'Доллар - {usd}\n'
                        f'Евро - {eur}',
                app_icon='icons/rate.ico',
                app_name='Notifyer',
                ticker ='asd',
                timeout=10
            )

        if kind == 'weather':
            city = data["Город"]
            weather = data["Погода"]
            temp = data["Температура"]
            wind = data["Ветер"]
            sunrise_time = data['Рассвет']
            sunset_time = data['Закат']

            ntf.notify(
                title=f'В городе {city} {weather}',
                message=f"Температура: {temp} °C\n"
                        f"Ветер: {wind} м/с\n"
                        f"Рассвет: {sunrise_time} Закат: {sunset_time}\n",
                app_icon='icons/weather.ico',
                timeout=10
            )

        if kind == 'news':
            article = str(list(data.keys())[-1])

            date = data[article]['Дата']
            title = data[article]['Заголовок']
            # link = data[article]['Ссылка']

            ntf.notify(
                title=f'Новость! {date}',
                message=f'{title}',
                app_icon='icons/news.ico',
                timeout=10
            )

