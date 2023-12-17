import os
import sys
from typing import List
from PyQt5 import QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
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
        self.buttonSelect.setStyleSheet(
            '''background: rgb(127, 255, 212);
            border-style: outset; 
            border-width: 5px;
            font-size: 24px;
            '''
            )
        
        self.buttonSelect.setFixedSize(500, 60)

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