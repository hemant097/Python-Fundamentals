import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont, QFontDatabase


#inheriting from QWidget class, not QMainWindow here
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)


        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;"
                                      "color: #0DCE15;"
                                      )
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("test_file/DS-DIGII.TTF") #loading the TTF file, it registers it with QT and returns an id (int)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] #as it returns a list
        my_font = QFont(font_family, 300)

        self.time_label.setFont(my_font)

        #connecting timer widget to a slot, so that it calls update_time(), every time it ticks
        self.timer.timeout.connect(self.update_time)
        #start the timer to tick every 1000ms
        self.timer.start(100)

        #calling the function once, so that there isn't a delay of 1 sec. Updates the UI immediately (no waiting)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss.zzz AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
