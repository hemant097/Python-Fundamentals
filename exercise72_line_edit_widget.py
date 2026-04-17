import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit",self)
        # self.button = QPushButton("Cancel",self)
        self.init_ui()

    def init_ui(self):
        self.line_edit.setGeometry(10,10,250,40)
        self.button.setGeometry(260,10,100,40)
        self.line_edit.setStyleSheet("background-color: lightgrey;"
                                     "font-size: 25px;"
                                     "font-family: Verdana;")
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.setStyleSheet("background-color: green;"
                                  "font-size: 18px;"
                                  "font-weight: bold;"
                                  "font-family: Arial;")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Hello {text}")

def main():
    app = QApplication(sys.argv) #for any command line arguments
    window = MainWindow()
    window.show() #else window closes within milliseconds
    sys.exit(app.exec_()) #execute method (.exec_ different from .exec

if __name__ == "__main__":
    main()