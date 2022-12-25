import sys
from PyQt5.QtWidgets import QApplication
from source.window import Window


def main():
    
    app = QApplication(sys.argv)
    window = Window()

    # Clean exit after window is closed
    sys.exit(app.exec())
