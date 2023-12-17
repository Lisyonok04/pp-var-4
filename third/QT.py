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
        self.buttonSelect.clicked.connect(self.getdataset)

        self.buttonCreate = QPushButton("Create annotasion for dataset", self)
        self.buttonCreate.setStyleSheet('''
                                        background: rgb(64, 234, 208);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 20px;
                                        ''')
        self.buttonCreate.setFixedSize(500, 60)
        self.buttonCreate.clicked.connect(self.create_csv)

        self.buttonNew = QPushButton("Create new dataset and annotasion for dataset", self)
        self.buttonNew.setStyleSheet('''
                                        background: rgb(30, 144, 255);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 20px;
                                        ''')
        self.buttonNew.setFixedSize(500, 60)
        self.buttonNew.clicked.connect(self.copy)

        self.buttonRandom = QPushButton("Create new random dataset and annotasion for dataset", self)
        self.buttonRandom.setStyleSheet('''
                                        background: rgb(65, 105, 225);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonRandom.setFixedSize(500, 60)
        self.buttonRandom.clicked.connect(self.random)

        self.buttonRose = QPushButton("Next rose", self)
        self.buttonRose.setStyleSheet('''
                                        background: rgb(218, 112, 214);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonRose.setFixedSize(500, 60)
        self.buttonRose.clicked.connect(self.next_rose)

        self.buttonTulip = QPushButton("Next tulip", self)
        self.buttonTulip.setStyleSheet('''
                                        background: rgb(147, 112, 219);
                                        border-style: outset; 
                                        border-width: 5px;
                                        font-size: 19px;
                                        ''')
        self.buttonTulip.setFixedSize(500, 60)
        self.buttonTulip.clicked.connect(self.next_tulip)

        self.label = QLabel(self)

        grid = QGridLayout()
        grid.setSpacing(2)

        grid.addWidget(self.buttonSelect, 0, 0)
        grid.addWidget(self.buttonCreate, 1, 0)
        grid.addWidget(self.buttonNew, 2, 0)
        grid.addWidget(self.buttonRandom, 3, 0)
        grid.addWidget(self.buttonRose, 4, 0)
        grid.addWidget(self.buttonTulip, 5, 0)
        grid.addWidget(self.label, 0, 1, 4, 1, alignment=Qt.AlignCenter)

        self.setLayout(grid)

        self.setWindowTitle("Flower blossom")
        self.setStyleSheet("background: rgb(220, 208, 255); font: 10pt Comic Sans MS")
        self.setWindowIcon(QIcon("Windowrose.jpg"))

    def messagebox(self, text: str) -> None:
        dlg = QDialog(self)
        dlg.setWindowTitle("Flower blossom")
        text = QLabel(text, dlg)
        btn = QPushButton("Ok", dlg)
        vbox = QVBoxLayout(dlg)
        vbox.addStretch(1)
        vbox.addWidget(text)
        vbox.addWidget(btn)
        btn.clicked.connect(dlg.close)
        dlg.exec()

    def getdataset(self) -> None:
        self.dirlist: str = QFileDialog.getExistingDirectory(self, "Select Folder")
        if os.path.exists(os.path.join("pp-var-4", "dataset", "rose")) | os.path.exists(
            os.path.join("dataset", "tulip")
        ):
            self.iter()
        else:
            self.messagebox("The folder is incorrectly selected.")

    def iter(self) -> None:
        self.rose: Iterator = Iterator("rose", self.dirlist)
        self.tulip: Iterator = Iterator("tulip", self.dirlist)
    
    def select(self) -> List[str]:
        """
        User's choice of folders.
        """
        paths: List[str] = []
        dirlist: str = QFileDialog.getExistingDirectory(self, "Select Folder")
        save_dir: str = QFileDialog.getExistingDirectory(self, "Select Folder For Save")
        paths.append(dirlist)
        paths.append(save_dir)
        return paths

    def create_csv(self) -> None:
        paths: List[str] = self.select()
        if os.path.exists(os.path.join(paths[0], "rose")) & os.path.exists(
            os.path.join(paths[0], "tulip")
        ):
            task1.create_csv(paths[0])
            task1.create_csv(paths[1])
            self.messagebox("The annotation have been created.")
        else:
            self.messagebox("The folder is incorrectly selected.")
    
    def copy(self) -> None:
        paths: List[str] = self.select()
        if os.path.exists(os.path.join(paths[0], "rose")) & os.path.exists(
            os.path.join(paths[0], "tulip")
        ):
            task2.copy_in_file(paths[0], "dataset2", "tulip")
            task2.copy_in_file(paths[1], "dataset2", "rose")
            self.messagebox("The dataset and annotation have been created.")
        else:
            self.messagebox("The folder is incorrectly selected.")

    def random(self) -> None:
        paths: List[str] = self.select()
        if os.path.exists(os.path.join(paths[0], "rose")) & os.path.exists(
            os.path.join(paths[0], "tulip")
        ):
            task3.copy_images(paths[0], "dataset3", "tulip")
            task3.copy_images(paths[1], "dataset3", "rose")
            self.messagebox("The dataset and annotation have been created.")
        else:
            self.messagebox("The folder is incorrectly selected.")

    def next_rose(self) -> None:
        rose_path: str = next(self.rose)
        if rose_path != None:
            image = QPixmap(rose_path)
            image_rez = image.scaledToHeight(240)
            self.label.setPixmap(image_rez)
        else:
            self.messagebox("The images of this class have ended.")
            self.iter()
            self.next_rose()

    def next_tulip(self) -> None:
        tulip_path: str = next(self.tulip)
        if tulip_path != None:
            image = QPixmap(tulip_path)
            image_rez = image.scaledToHeight(240)
            self.label.setPixmap(image_rez)
        else:
            self.messagebox("The images of this class have ended.")
            self.iter()
            self.next_tulip()

    
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