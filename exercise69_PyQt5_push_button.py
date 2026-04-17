import sys
from PyQt5.QtWidgets import  QMainWindow, QApplication, QPushButton, QLabel

#signal is an event. The slot is an action that the widget will take when that signal occurs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.button = QPushButton("Click me",self) #instance variable
        self.label = QLabel("Hello",self) #can be accessed anywhere inside class
        self.initUI()

    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;"
                                  "color: green;")
        #with button, we need a signal connected to a slot, here clicked is signal and slot is on_click
        self.button.clicked.connect(self.on_click) #passing a reference to the on_click, if we do on_click(),
                                                    # it will give TypeError, as will try to call the method
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("button clicked")

        #changing button text and style, disabling on clicking
        self.button.setText("Clicked")
        self.button.setStyleSheet("font-size: 30px; color: red;")
        self.button.setDisabled(True) #disables the method

        #changing label style
        self.label.setStyleSheet("font-size: 50px; color: blue;")
        self.label.setText("Goodbye!")





def main():
    app = QApplication(sys.argv) #for any command line arguments
    window = MainWindow()
    window.show() #else window closes within milliseconds
    sys.exit(app.exec_()) #execute method (.exec_ different from .exec

if __name__ == "__main__":
    main()
