import sys

from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)

        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)

        self.timer = QTimer(self)

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
                    QPushButton, QLabel{
                        padding: 10px 35px;
                        font-weight: bold;
                        font-family: calibri;
                    }
                    QPushButton {
                        font-size: 40px;
                        font-family: Futura;
                        margin: 5px;
                        border: 2px solid;
                        border-radius: 5px;     
                    }
                    
                    QPushButton:hover{
                        background-color: #A64444
                    } 
                    
                    QLabel{
                        font-size: 100px;
                        color: #0DCE15;
                        background-color: black;
                        border-radius: 10px;
                    }
                    """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #connecting timer widget to a slot, so that it calls update_time(), every time it ticks
        self.timer.timeout.connect(self.update_time)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() //10 #so get milliseconds in 2 digits only
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_time(self):

        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    stop_watch = Stopwatch()
    stop_watch.show()
    sys.exit(app.exec_())
