import os
import shutil
import csv
import random
from typing import List


def copy_images(old: str, new: str, name: str) -> None:
    """
    This function accepts name of the old dir, new one and the name of the class.

    The function thus copies files from the old directory to the new one, 
    adding the class name to each file, and creates entries in a CSV file 
    with absolute and relative paths, as well as the class name for each copied file.
    It also changes names of images for random number.
    """
    abs_path: str = os.path.abspath(new)
    rel_path: str = os.path.relpath(new)
    random_number: name = random.sample((range(0, 10000)), 2000)
    count: int = 0
    path: str = os.path.join(os.path.abspath(old), name)
    list_images: name = os.listdir(path)
    for img in list_images:
        new_name: str = f"{random_number[count]}".zfill(5)
        shutil.copy(
            os.path.join(path, img), os.path.join(new, f"{new_name}.jpg")
        )
        with open("Annotasion3.csv", "a") as f:
            filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
            filewriter.writerow(
                [
                    os.path.join(abs_path, f"{new_name}.jpg"),
                    os.path.join(rel_path, f"{new_name}.jpg"),
                    name,
                ]
            )
            count += 1


def creating_csvfile(namecsv: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the layout template of the elements. 
    """
    with open("Annotasion3.csv", "w", newline="") as f:
        filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])


if __name__ == "__main__":
    creating_csvfile("Annotasion3")
    copy_images("dataset", "dataset3", "tulip")
    copy_images("dataset", "dataset3", "rose")
