import csv
import shutil
import os
from typing import List

def copy_in_file(old: str, new: str, name: str) -> None:
    abs_path: str = os.path.abspath(new)
    rel_path: str = os.path.relpath(new)
    path: str = os.path.join(os.path.abspath(old), name)
    list_images: name = os.listdir(path)
    for img in list_images:
        shutil.copy(os.path.join(path, img), os.path.join(new, f"{name}_{img}"))
        with open("Annotasion2.csv", "a") as f:
            printer = csv.writer(f, delimiter=" ")
            #printer.writerow(["The Absolute Way", "Relative Way", "Class"])
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
    with open("Annotasion2.csv", "w", newline="") as f:
        filewriter = csv.writer(f, delimiter=" ", lineterminator="\r")
        filewriter.writerow(["Absolute path", "Relative path", "Class name"])



def create_another_relative_way(name_class: str, number: int) -> str:
    return f"dataset2/{name_class}_{str(number).zfill(4)}.jpg"

if __name__ == "__main__":
    creating_csvfile("Annotasion2.csv")
    copy_in_file("dataset", "dataset2", "tulip")
    copy_in_file("dataset", "dataset2", "rose")