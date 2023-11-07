import requests
from datetime import datetime


class WeatherParser:
    def __init__(self, token):
        self.token = token
        self.emoji = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B",
        }

    def get_weather(self, city: str) -> dict or str:
        """Получаем погоду"""

        try:
            cords_response = requests.get(
                f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={self.token}"
            )

        except Exception as ex:
            return f"Проверьте название города! {ex}"

        data = cords_response.json()
        coords = (data[0]["lat"], data[0]["lon"])
        lat, lon = coords

        try:
            weather_response = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.token}&units=metric"
            )
        except Exception as ex:
            return ex

        data = weather_response.json()

        city = data["name"]
        temp = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        weather_description = data["weather"][0]["main"]

        if weather_description in self.emoji:
            weather_description = self.emoji[weather_description]

        # В api есть пункты с извержением вулканов и пеплом
        else:
            weather_description = "Там что-то ужасное"

        sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.fromtimestamp(data["sys"]["sunset"])

        result = {
            "Город": city,
            "Погода": weather_description,
            "Температура": temp,
            "Давление": pressure,
            "Влажность": humidity,
            "Ветер": wind,
            "Рассвет": sunrise_time.strftime("%H:%M:%S"),
            "Закат": sunset_time.strftime("%H:%M:%S"),
        }

        return result
