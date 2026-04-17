import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup, QWidget, QVBoxLayout, QGroupBox


# By default, unless explicitly stated are all part of the same group, i.e., we can only choose one of them, what if we need to choose like
# Need to choose one from them
#       Bread Parmesan
#       Bread Wheat
# and one from them
#       Mint Mayo
#       Mustard Sauce
#then we require button groups

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 600, 600)
        self.radio1 = QRadioButton("Visa",self)
        self.radio2 = QRadioButton("MasterCard",self)
        self.radio3 = QRadioButton("RuPay",self)
        self.radio4 = QRadioButton("Gift-Card", self)
        self.radio5 = QRadioButton("In-store", self)

        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

        """setting the stylesheet on all QRadioButton"""
        self.setStyleSheet("QRadioButton{"
                           "font-size: 20px; font-family: Verdana;"
                           "padding: 10px"
                           "}")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()  # generic widget
        self.setCentralWidget( central_widget )

        # subway breads
        bread1 = QRadioButton("Hearty Italian")
        bread2 = QRadioButton("Honey Oat")
        bread3 = QRadioButton("Multi grain")
        bread4 = QRadioButton("Gluten free")

        # sauces
        sauce1 = QRadioButton("Marinara")
        sauce2 = QRadioButton("Sweet Onion")
        sauce3 = QRadioButton("Chipotle")
        sauce4 = QRadioButton("Barbecue")
        sauce5 = QRadioButton("Mustard")

        # veggies
        veggie1 = QRadioButton("Capsicum")
        veggie2 = QRadioButton("Onion")
        veggie3 = QRadioButton("Tomato")
        veggie4 = QRadioButton("Jalapeno")

        """ As we are using layout thus no need for setting geometry"""
        # bread1.setGeometry( 0, 250, 300, 50 )
        # bread2.setGeometry( 0, 275, 300, 50 )
        # bread3.setGeometry( 0, 300, 300, 50 )
        # bread4.setGeometry( 0, 325, 300, 50 )
        #
        # veggie1.setGeometry( 0, 350, 300, 50 )
        # veggie2.setGeometry( 0, 375, 300, 50 )
        # veggie3.setGeometry( 0, 400, 300, 50 )
        # veggie4.setGeometry( 0, 425, 300, 50 )
        #
        # sauce1.setGeometry( 0, 450, 300, 50 )
        # sauce2.setGeometry( 0, 475, 300, 50 )
        # sauce3.setGeometry( 0, 500, 300, 50 )
        # sauce4.setGeometry( 0, 525, 300, 50 )
        # sauce5.setGeometry( 0, 550, 300, 50 )

        #  QButtonGroup (logic only)
        #  Not visible on screen
        #  Cannot be added to a layout
        #  Used to control button behavior

        #to use buttonClicked.connect, we need to use self in button groups, else program crashes with Process finished with exit code -1073740791 (0xC0000409)
        # possibly QButtonGroup was getting destroyed, But Qt still tries to use it (because of signal connection)
        self.button_group_breads = QButtonGroup(self)
        self.button_group_sauces = QButtonGroup(self)
        self.button_group_veggies = QButtonGroup(self)

        # adding buttons to their respective groups
        self.button_group_breads.addButton( bread1 )
        self.button_group_breads.addButton( bread2 )
        self.button_group_breads.addButton( bread3 )
        self.button_group_breads.addButton( bread4 )

        self.button_group_sauces.addButton( sauce1 )
        self.button_group_sauces.addButton( sauce2 )
        self.button_group_sauces.addButton( sauce3 )
        self.button_group_sauces.addButton( sauce4 )
        self.button_group_sauces.addButton( sauce5 )

        self.button_group_veggies.addButton( veggie1 )
        self.button_group_veggies.addButton( veggie2 )
        self.button_group_veggies.addButton( veggie3 )
        self.button_group_veggies.addButton( veggie4 )

        # bread1.toggled.connect(self.radio_button_changed)
        # bread2.toggled.connect(self.radio_button_changed)

        self.button_group_breads.buttonClicked.connect(self.radio_group_button_changed)
        self.button_group_veggies.buttonClicked.connect(self.radio_group_button_changed)
        self.button_group_sauces.buttonClicked.connect(self.radio_group_button_changed)

        # Main layout
        main_layout = QVBoxLayout()

        # 📦 QGroupBox (visual container)
        #  Visible box with a title
        #  Can be added to layouts
        #  Used to organize UI sections
        #  It holds widgets inside it

        # group box (visible container)
        group_box_bread = QGroupBox("Choose one bread from each")
        group_box_veggies = QGroupBox("Choose one veggie from each")
        group_box_sauces = QGroupBox("Choose one sauce from each")

        # Layout inside group box
        breads_layout = QVBoxLayout()
        veggies_layout = QVBoxLayout()
        sauces_layout = QVBoxLayout()

        #adding each item in specific VBoxLayout
        breads_layout.addWidget( bread1 )
        breads_layout.addWidget( bread2 )
        breads_layout.addWidget( bread3 )
        breads_layout.addWidget( bread4 )

        veggies_layout.addWidget( veggie1 )
        veggies_layout.addWidget( veggie2 )
        veggies_layout.addWidget( veggie3 )
        veggies_layout.addWidget( veggie4 )

        sauces_layout.addWidget( sauce1 )
        sauces_layout.addWidget( sauce2 )
        sauces_layout.addWidget( sauce3 )
        sauces_layout.addWidget( sauce4 )
        sauces_layout.addWidget( sauce5 )

        # adding VBoxLayout to their specific group box
        group_box_bread.setLayout( breads_layout )
        group_box_veggies.setLayout(veggies_layout)
        group_box_sauces.setLayout(sauces_layout)

        # adding all the group boxes to the main layout
        main_layout.addWidget( group_box_bread )
        main_layout.addWidget( group_box_veggies )
        main_layout.addWidget( group_box_sauces )

        # adding main layout to central widget
        central_widget.setLayout(main_layout)

        #We added a giant vbox into central widget
        #   added 3 group boxes into that giant vbox
        #       inside each group box, we have one small vbox ( for displaying radio buttons)
        #           inside each small vbox we have radio buttons (as button groups cannot be added )


    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

    def radio_group_button_changed(self,button):
        if button.isChecked():
            print(f"{button.text()} is clicked")



def main():
    app = QApplication(sys.argv) #for any command line arguments
    window = MainWindow()
    window.show() #else window closes within milliseconds
    sys.exit(app.exec_()) #execute method (.exec_ different from .exec

if __name__ == "__main__":
    main()
