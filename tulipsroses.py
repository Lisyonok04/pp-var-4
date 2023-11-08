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

def pic_links(request: str) -> None:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://yandex.ru/images/search?text={request}"
    driver.get(url = url)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(
        By.CSS_SELECTOR, 'div.serp-item__preview a.serp-item__link').click()
    with open(f"{request}.txt", 'w') as file:
        for i in range(10):
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


def main() -> None:

    if os.path.isdir("dataset"):
        shutil.rmtree("dataset")
    request = "rose"
    pic_links(request)
    make_folder("dataset")
    make_folder(f"dataset/{request}")
    request = "tulips"
    pic_links(request)
    make_folder("dataset")
    make_folder(f"dataset/{request}")