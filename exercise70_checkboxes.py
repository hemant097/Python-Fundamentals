import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox


#signal is an event. The slot is an action that the widget will take when that signal occurs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.checkbox = QCheckBox("Do you like pizza",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Verdana;")
        self.checkbox.stateChanged.connect(self.checkbox_change)

    def checkbox_change(self, state):
        # if state == 2: when box is checked state is 2, when unchecked state is 0
        if state == Qt.CheckState.Checked: #this also is 2
            print("You like pizza")
        elif state == Qt.CheckState.Unchecked:
            print("You are bad, you don't like pizza")





def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
