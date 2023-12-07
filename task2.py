import csv
import os
from typing import List

def write_in_file(name_class: str, number: int) -> None:

    with open("dataset.csv", "a", newline='', encoding='utf8') as file:
        printer = csv.writer(file, delimiter=";")
        printer.writerow(
            [os.path.abspath(create_another_relative_way(name_class, number)),
             create_another_relative_way(name_class, number),
             name_class]
        )


def create_csv(namecsv: str) -> None:
    num_files = len([f for f in os.listdir(namecsv + "/tulip")
                     if os.path.isfile(os.path.join(namecsv + "/tulip", f))])
    with open("dataset.csv", "w", newline='') as file:
        printer = csv.writer(file, delimiter=";", )
        printer.writerow(["The Absolute Way", "Relative Way", "Class"])
    for i in range(0, num_files):
        name_class = "tulip"
        way = f"{namecsv}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)
        name_class = "rose"
        way = f"{namecsv}/{name_class}/{str(i).zfill(4)}.jpg"
        if os.path.isfile(way):
            write_in_file(name_class, i)

def create_another_relative_way(name_class: str, number: int) -> str:
    return f"dataset/{name_class}_{str(number).zfill(4)}.jpg"

if __name__ == "__main__":
    create_csv("dataset")