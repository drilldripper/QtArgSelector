from argument_selector import ArgumentSelector
from PyQt5.QtWidgets import (QApplication)
import sys

if __name__ == '__main__':
    # Launch PyQt Application
    app = QApplication(sys.argv)
    # Instantiate GUI
    ex = ArgumentSelector()
    app.exec_()
    # Check Arguments
    print(sys.argv)

