from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
                            QLabel, QPushButton,
                            QVBoxLayout, QHBoxLayout,
                            QFrame)
from PyQt5.QtCore import Qt


class Window(QWidget):

    def __init__(self):
        
        super().__init__()
        
        self.InitWindow()
        self.InitUI()
        self.show()

    
    def InitWindow(self):

        self.setFixedSize(475, 350)
        self.setWindowTitle("RPS GAME")
        # self.setWindowIcon(QIcon("assets/PIXELA_ORIGINAL_e.png"))


        qRectangle = self.frameGeometry()
        centerpoint = QDesktopWidget().availableGeometry().center()
        qRectangle.moveCenter(centerpoint)
        self.move(qRectangle.topLeft())


    def InitUI(self):

        vbox_main = QVBoxLayout()
        cpu_hbox = QHBoxLayout()
        cpu_hbox.setAlignment(Qt.AlignCenter)
        user_hbox = QHBoxLayout()
        user_hbox_frame = QFrame()
        user_hbox_frame.setLayout(user_hbox)


        self.rock_button = QPushButton("ROCK")

        self.paper_button = QPushButton("PAPER")

        self.scissors_button = QPushButton("SCISSORS")

        self.cpu_choice_text = QLabel("Cpu is thinking...")

        user_hbox.addWidget(self.rock_button)
        user_hbox.addWidget(self.paper_button)
        user_hbox.addWidget(self.scissors_button)
        cpu_hbox.addWidget(self.cpu_choice_text)


        vbox_main.addLayout(cpu_hbox)
        vbox_main.addWidget(user_hbox_frame)

        self.setLayout(vbox_main)