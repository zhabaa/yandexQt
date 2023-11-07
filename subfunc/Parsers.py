from subfunc.Weather import WeatherParser
from subfunc.Rate import RateParser
from subfunc.News import NewsParser


class Parse:
    def __init__(self):
        self.path_to_tokens = "D:/python/notifier/subfunc/tokens"
        

    def parse_news(self):
        """Новости"""
        with open(f"{self.path_to_tokens}/news_token.txt", "r", encoding="utf-8") as file:
            newstoken = file.read()
        
        self.NewsParser = NewsParser(newstoken)
        result = self.NewsParser.get_news()
        
        return result


    def parse_rate(self):
        """Курсы валют USD и EUR"""
        with open(f"{self.path_to_tokens}/rates_token.txt", "r", encoding="utf-8") as file:
            ratetoken = file.read()
            
        self.RateParser = RateParser(ratetoken)
        result = self.RateParser.get_rate()
        
        return result

    def parse_weather(self, city):
        """Погода"""
        with open(f"{self.path_to_tokens}/weather_token.txt", "r", encoding="utf-8") as file:
            weathertoken = file.read()

        self.WeatherParser = WeatherParser(weathertoken)
        result = self.WeatherParser.get_weather(city)
        
        return result

