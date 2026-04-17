import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget() #generic widget
        self.setCentralWidget(central_widget)

        #as we're setting central_widget to self, thus label = QLabel("",self) is not required here
        label1 = QLabel("Monica")
        label2 = QLabel("Oh")
        label3 = QLabel("My")
        label4 = QLabel("Darling")
        label5 = QLabel("Yeehaw")
        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:green")
        label3.setStyleSheet("background-color:blue")
        label4.setStyleSheet("background-color:yellow")
        label5.setStyleSheet("background-color:purple")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,1,2)


        #setting the layout of central widget with the layout manager of grid/vbox, and this central widget will be added to main window
        central_widget.setLayout(grid)








def main():
    app = QApplication(sys.argv) #for any command line arguments
    window = MainWindow()
    window.show() #else window closes within milliseconds
    sys.exit(app.exec_()) #execute method (.exec_ different from .exec

if __name__ == "__main__":
    main()
