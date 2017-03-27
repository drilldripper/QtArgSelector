from arg_prompt import ArgumentSelector
from PyQt5.QtWidgets import (QApplication)
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArgumentSelector()
    app.exec_()
    print(sys.argv)

