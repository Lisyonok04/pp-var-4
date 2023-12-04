import requests
import os
import shutil
import time
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def is_image(data):
    try:
        Image.open(BytesIO(data))
        return True
    except:
        return False

def make_folder(name: str) -> None:

    if not os.path.isdir(name):
        os.mkdir(name)

def pic_links(name: str, count: int) -> None:
    chrome_driver_path = "D:/chromedriver/chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())) 
    url = f"https://yandex.ru/images/search?text={name}" 
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "a.Link.SimpleImage-Cover").click()

    with open(f"urls_for_{name}.txt", 'w') as file:
        for i in range(count):
            try:
                time.sleep(0.5)
                link = driver.find_element(
                    By.CSS_SELECTOR, "a.Button2_view_action").get_attribute("href")
                file.write(link + '\n')
                driver.find_element(
                    By.CSS_SELECTOR, "div.CircleButton:nth-child(4)").click()
            except:
                continue

    driver.close()
    driver.quit()
    


def download(name: str, path: str) -> None:
    make_folder(f"{path}")
    with open(f"urls_for_{name}.txt", 'r') as file:
        reader = file.read().split("\n")
        count = 0
        for item in reader:
            try:
                count += 1
                img = requests.get(str(item))
                if is_image(img.content):
                    img_file = open(f'{path}/{name}{count}.jpeg', 'wb')
                    img_file.write(img.content)
                    img_file.close()
                time.sleep(0.2)
            except:
                continue


def parse(name: str, count: int, folder: str):
    pic_links(name, count)
    download(name, folder)


def main() -> None:
    if os.path.isdir("dataset"):
        shutil.rmtree("dataset")
    if os.path.isdir("__pycache__"):
        shutil.rmtree("__pycache__")
    parse("tulip", 1000, "tulip")
    parse("rose", 1000, "rose")