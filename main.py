import sys
import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from UsersDataBase import DataBase
from subfunc.Notify import ShowNotify
from subfunc.Parsers import Parse
from subfunc.MyExceptions import MyException

if hasattr(QtCore.Qt, "AA_EnableHighDpiScaling"):
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, "AA_UseHighDpiPixmaps"):
    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class MyProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("test.ui", self)
        self.initUI()

        self.DBase = DataBase()
        self.parser = Parse()
        self.notify = ShowNotify()

    def initUI(self):
        self.signin_btn.clicked.connect(self.sign)
        self.signup_btn.clicked.connect(self.sign)
        self.update_btn.clicked.connect(self.update)
        self.setCentralWidget(self.stackedWidget)

    def get_login_and_pass(self) -> tuple[str]:
        """Получить логины и пароли из базы данных"""
        login = self.login_input.text()
        password = self.password_input.text()
        return (login, password)

    def to_mainPage(self) -> None:
        """Перейти на главную страницу"""
        self.stackedWidget.setCurrentWidget(self.mainPage)
        self.statusbar.showMessage("")

    def check_password(self, password: str) -> bool:
        """Функция проверки пароля"""
        first = len(password) > 6
        return first

    def sign(self) -> None:
        """Основной функционал начального меню и кнопок sign in / sign up"""
        login, password = self.get_login_and_pass()
        db_info = self.DBase.get_info()

        #  -//- sign in
        if self.sender() is self.signin_btn:
            try:
                if login not in db_info.keys():
                    self.statusbar.showMessage("Login does not exist")

                elif db_info[login] != password:
                    self.statusbar.showMessage("Incorrect password")

                else:
                    self.to_mainPage()

            except Exception as ex:
                print(ex)

        #  -//- sign up
        else:
            try:
                if self.check_password(password):
                    self.DBase.add_user(login, password)
                    self.to_mainPage()
                else:
                    self.statusbar.showMessage("Bad password")

            except sqlite3.IntegrityError:
                self.statusbar.showMessage("This login is used")

    def update(self):
        self.statusbar.showMessage("Wait a few second ~")
        
        city = self.city_input.text()
        try:
            rate_data = self.parser.parse_rate()
        except Exception as ex:
            self.statusbar.showMessage(f'[Err] currency parsing failed\n {ex}')

        try:
            weather_data = self.parser.parse_weather(city)
        except Exception as ex:
            self.statusbar.showMessage(f'[Err] weather parsing failed\n {ex}')
            # if not isinstance(weather_data, dict):
            #     raise MyException(city)

        try:
            news_data = self.parser.parse_news()
        except Exception as ex:
            self.statusbar.showMessage(f'[Err] news parsing failed\n {ex}')
            
        usd = rate_data['USD']
        eur = rate_data['EUR']
        
        city = weather_data["Город"]
        weather = weather_data["Погода"]
        temp = weather_data["Температура"]
        wind = weather_data["Ветер"]
        sunrise_time = weather_data['Рассвет']
        sunset_time = weather_data['Закат']
        
        article = str(list(news_data.keys())[-1])
        
        date = news_data[article]['Дата']
        title = news_data[article]['Заголовок']
        link = news_data[article]['Ссылка']


        result = f"""
        Курс:
        Доллар - {usd}
        Евро - {eur}
        
        Погода городе {city} {weather}
        Температура: {temp} °C
        Ветер: {wind} м/с
        Рассвет: {sunrise_time} Закат: {sunset_time}

        Новость! - {date}
        Заголовок: {title}
        Ссылка: {link}
        """

        self.info_output.setText(result)
        
    
    def show_notify(self):
        # while True 
        pass

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainform = MyProgram()
    mainform.show()
    sys.excepthook = except_hook
    sys.exit(application.exec())
