class MyException(Exception):
    def __init__(self, data: type) -> None:
        self.data = data

    def __str__(self) -> str:
        if isinstance(self.data, dict):
            return "[Er] Проверьте название города и повторите попытку"
