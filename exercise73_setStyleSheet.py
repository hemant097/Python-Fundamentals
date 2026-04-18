import sys
from PyQt5.QtWidgets import QApplication, QMainWindow ,QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        central_widget.setLayout(hbox)

        #setting CSS for all buttons, and one button
        self.setStyleSheet("""
            QPushButton {
                font-size: 32px;
                font-family: Futura;
                padding: 15px 75px;
                margin: 25px;
                border: 2px solid;
                border-radius: 10px;     
            }
            
            QPushButton#button1{
                background-color: red; 
            } 
            QPushButton#button2{
                background-color: #ff5577; 
            } 
            QPushButton#button3{
                background-color: #ffeacf; 
            } 
            
            QPushButton#button1:hover{
                 background-color: #A64444
            } 
            QPushButton#button2:hover{
                background-color: #44A644; 
            } 
            QPushButton#button3:hover{
                background-color: #4444A6; 
            } 
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()