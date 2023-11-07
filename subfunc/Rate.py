import requests


class RateParser:
    def __init__(self, token) -> None:
        self.token = token

    def get_rate(self) -> dict:
        """Получаем курсы валют USD и EUR"""

        try:
            response = requests.get(
                f"https://v6.exchangerate-api.com/v6/{self.token}/latest/RUB"
            )
        except Exception as ex:
            return ex

        data = response.json()

        usd = data["conversion_rates"]["USD"]
        eur = data["conversion_rates"]["EUR"]

        result = {"USD": round(1 / usd, 2), "EUR": round(1 / eur, 2)}

        return result
