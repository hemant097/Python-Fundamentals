import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from requests import HTTPError, RequestException, TooManyRedirects

from test_file.api_key import API_KEY

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel,QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size:40px;
                font-style:italic;
            }
            QLineEdit#city_input{
                font-size:40px;
            } 
            QPushButton#get_weather_button{
                font-size:30px;
                font-weight:bold;
            }
            QLabel#temperature_label{
                font-size:75px;
            }
            
            QLabel#emoji_label{
                font-size:100px;
                font-family:Segoe UI emoji;
            }
            
            QLabel#description_label{
                font-size:50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        city = self.city_input.text() #get the user input
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

        response = requests.get(url)
        try:
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)
        except HTTPError as http_err:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check you input")
                case 401:
                    self.display_error("Unauthorized request:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is Denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP Error:\n{http_err}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nPlease check your internet connection")

        except requests.exceptions.Timeout :
            self.display_error("Timeout Error:\n The request timed out")

        except TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the url")
        except RequestException:
            self.display_error(f"Request Error:\nPlease check your internet connection")



    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        #clearing the previous data when we get an error
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data['main']['temp']
        temperature_c = temperature_k-273.15
        temperature_f = round(temperature_c*1.8+32)

        weather_description = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']

        self.temperature_label.setText(f"{temperature_c:.2f} °C")
        self.description_label.setText(f"{weather_description}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        print(f"weather_id: {weather_id}")

        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "⛅"
        elif 500 <= weather_id <=531:
            return "☁️"
        elif 600 <= weather_id <=622:
            return "❄️"
        elif 700 <= weather_id <=761:
            return "💨"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "🌪️"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "⛅"
        else:
            return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_()) #exec handles events in our window