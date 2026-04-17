import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") #set window title
        self.setGeometry(300, 300, 500, 500) #x,y,width,height
        self.setWindowIcon(QIcon("test_file/Screenshot 2026-04-17 130627.jpg"))


def main():
    app = QApplication(sys.argv) #for any command line arguments
    window = MainWindow()
    window.show() #else window closes within milliseconds
    sys.exit(app.exec_()) #execute method (.exec_ different from .exec

if __name__ == "__main__":
    main()
