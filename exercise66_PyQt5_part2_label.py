import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont #for fonts
from PyQt5.QtCore import Qt #used for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI") #set window title
        self.setGeometry(300, 300, 500, 500) #x,y,width,height

        label = QLabel("Hello",self)
        label.setFont(QFont("Verdana", 20))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #782e2e;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) #align vertically top
        label.setAlignment(Qt.AlignmentFlag.AlignBottom) #align vertically bottom
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter) #align vertically center (DEFAULT)
        label.setAlignment(Qt.AlignmentFlag.AlignRight) # horizontally right
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter) #horizontally center
        label.setAlignment(Qt.AlignmentFlag.AlignLeft) #horizontally left

        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop) #center and top
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom) # center and bottom
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) #combines HCenter and VCenter






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
