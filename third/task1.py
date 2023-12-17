import csv
import os
from typing import List

def write_in_file(name_class: str, number: int) -> None:

    """
    This function accepts the name of the class and the photo number.

    The function writes information about the file to a csv file. 
    It opens the Annotasion.csv and adds a new line containing 
    the absolute path to the file, the relative path to the file, 
    and the class name.

    """
    with open("Annotasion.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=" ", lineterminator="\r")
        printer.writerow(
            [os.path.abspath(create_relative_way(name_class, number)),
             create_relative_way(name_class, number),
             name_class]
        )


def create_csv(namecsv: str) -> None:
    """
    This function accepts the name of csv-file.

    The function opens a csv file and fills it with information about the files. 
    At first, it opens the Annotasion.csv file and writes the title and the layout template of the elements. 
    After that, it goes through the files in the tulip and rose folders, and if the file exists, 
    calls the write_in_file function to write information more about the file to a csv file.

    """
    with open("Annotasion.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=" ", lineterminator="\r")
        printer.writerow(["The Absolute Way", "Relative Way", "Class name"])
    for i in range(0, 2000):
        name_class = "tulip"
        way = f"{namecsv}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)
        name_class = "rose"
        way = f"{namecsv}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)

def create_relative_way(name_class: str, number: int) -> str:
    """
    This function accepts the name of the class and the number of the picture.
    
    It creates a relative path to the file using the class name and file number.
    """
    return f"dataset/{name_class}/{str(number).zfill(4)}.jpg"

if __name__ == "__main__":
    create_csv("dataset")