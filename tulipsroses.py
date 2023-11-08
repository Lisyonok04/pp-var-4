import os
import shutil
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def make_folder(name: str) -> None:

    if not os.path.isdir(name):
        os.mkdir(name)




def main() -> None:
    if os.path.isdir("dataset"):
        shutil.rmtree("dataset")
    make_folder("dataset")
    request = "rose"
    make_folder(f"dataset/{request}")

    