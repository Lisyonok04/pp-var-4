import csv
import shutil
import os
from typing import List


def copy_in_file(old: str, new: str, name: str) -> None:
    """
    This function accepts name of the old dir, new one and the name of the class.

    The function thus copies files from the old directory to the new one, 
    adding the class name to each file, and creates entries in a CSV file with absolute and relative paths, as well as the class name for each copied file.
    """
    abs_path: str = os.path.abspath(new)
    rel_path: str = os.path.relpath(new)
    path: str = os.path.join(os.path.abspath(old), name)
    list_images: name = os.listdir(path)
    for img in list_images:
        shutil.copy(os.path.join(path, img),
                    os.path.join(new, f"{name}_{img}"))
        with open("Annotasion2.csv", "a") as f:
            printer = csv.writer(f, delimiter=",")
            printer.writerow(
                [
                    os.path.join(abs_path, f"{name}_{img}"),
                    os.path.join(rel_path, f"{name}_{img}"),
                    name,
                ]
            )


def creating_csvfile(namecsv: str) -> None:
    """
    The function takes as input the name for the .csv file,
    creates a .csv file with the passed name and writes the column headers.
    """
    with open("Annotasion2.csv", "w", newline='') as f:
        filewriter = csv.writer(f, delimiter=",")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])


if __name__ == "__main__":
    creating_csvfile("Annotasion2.csv")
    copy_in_file("dataset", "dataset2", "tulip")
    copy_in_file("dataset", "dataset2", "rose")
