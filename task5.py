import os
from typing import List

class Iterator:
    def __init__(self, class_name: str):
        self.class_name: str = class_name
        self.counter: int = 0
        self.data: List[str] = os.listdir(os.path.join("dataset", class_name))
        self.limit: int = len(self.data)
    def __next__(self):
        if self.counter < self.limit:
            path: str = os.path.join(
                "dataset1", self.class_name, self.data[self.counter]
            )
            self.counter += 1
            return path
        else:
            raise StopIteration

if __name__ == "__main__":
    class_name: Iterator = Iterator("rose")

    for _ in range(5):
        print(next(class_name))

    class_name: Iterator = Iterator("tulip")

    for _ in range(5):
        print(next(class_name))