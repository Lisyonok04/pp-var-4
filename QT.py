import os
import sys
from typing import List
from PyQt5 import QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import task1
import task2
import task3
from task5 import Iterator

class Interface(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    def initUI(self) -> None:
        self.buttonSelect = QPushButton("Select dataset", self)
        self.buttonSelect.setStyleSheet('''
                                        background: rgb(127, 255, 212);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 20px;
                                         ''')
        self.buttonSelect.setFixedSize(500, 60)

        self.buttonCreate = QPushButton("Create annotasion for dataset", self)
        self.buttonCreate.setStyleSheet('''
                                        background: rgb(102, 205, 170);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 20px;
                                        ''')
        self.buttonCreate.setFixedSize(500, 60)

        self.buttonNew = QPushButton("Create new dataset and annotasion for dataset", self)
        self.buttonNew.setStyleSheet('''
                                        background: rgb(64, 224, 208);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 20px;
                                        ''')
        self.buttonNew.setFixedSize(500, 60)

        self.buttonRandom = QPushButton("Create new random dataset and annotasion for dataset", self)
        self.buttonRandom.setStyleSheet('''
                                        background: rgb(72, 209, 204);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonRandom.setFixedSize(500, 60)

        self.buttonRose = QPushButton("Next rose", self)
        self.buttonRose.setStyleSheet('''
                                        background: rgb(0, 206, 209);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonRose.setFixedSize(500, 60)

        self.buttonTulip = QPushButton("Next tulip", self)
        self.buttonTulip.setStyleSheet('''
                                        background: rgb(0, 255, 255);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonTulip.setFixedSize(500, 60)


def main() -> None:
    """
    An application object is being created.
    """
    app = QApplication(sys.argv)
    ex = Interface()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()