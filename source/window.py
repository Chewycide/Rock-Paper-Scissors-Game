from PyQt5.QtWidgets import (
    QWidget,
    QDesktopWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QMessageBox
    )
from PyQt5.QtCore import Qt
from source.game import Game
import random as rd


class Window(QWidget):
    """
        Window class renders the window that the application will
        be embedded in 
    """
    def __init__(self):
        
        super().__init__()
        
        
        self.InitWindow()
        self.InitUI()
        self.show()

    
    def InitWindow(self):
        """Initialize the window size and screen position"""

        self.setFixedSize(475, 350)
        self.setWindowTitle("RPS GAME")


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def InitUI(self):
        """Initialize the User Interface"""

        self.outcome_popup = QMessageBox()
        self.outcome_popup.setWindowTitle(" ")


        vbox_main = QVBoxLayout()
        cpu_hbox = QHBoxLayout()
        cpu_hbox.setAlignment(Qt.AlignCenter)
        user_hbox = QHBoxLayout()
        user_hbox_frame = QFrame()
        user_hbox_frame.setLayout(user_hbox)


        self.rock_button = QPushButton("ROCK")
        self.rock_button.clicked.connect(self.rock)


        self.paper_button = QPushButton("PAPER")
        self.paper_button.clicked.connect(self.paper)


        self.scissors_button = QPushButton("SCISSORS")
        self.scissors_button.clicked.connect(self.scissors)


        self.cpu_choice_text = QLabel("Cpu is thinking...")


        user_hbox.addWidget(self.rock_button)
        user_hbox.addWidget(self.paper_button)
        user_hbox.addWidget(self.scissors_button)
        cpu_hbox.addWidget(self.cpu_choice_text)


        vbox_main.addLayout(cpu_hbox)
        vbox_main.addWidget(user_hbox_frame)

        self.setLayout(vbox_main)

    
    def rock(self):
        """This method executes when ROCK button is pressed"""
        return self.rps(0)


    def paper(self):
        """This method executes when PAPER button is pressed"""
        return self.rps(1)


    def scissors(self):
        """This method executes when SCISSORS button is pressed"""
        return self.rps(2)

    
    def rps(self, choice):
        """
            Displays a popup displaying the outcome of the round
        """
        self.cpu_choice = rd.randint(0, 2)

        rps_game = Game()
        self.cpu_choice_text.setText(rps_game.cpu_choice_func(self.cpu_choice))

        self.outcome_popup.setText(rps_game.game_outcome(choice, self.cpu_choice))
        return self.outcome_popup.exec()
        