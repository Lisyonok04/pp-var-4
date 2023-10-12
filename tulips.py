import os
import requests
import simplejson as json
from bs4 import BeautifulSoup
import cv2

def download_images(query, folder, num_images):
    url = "https://yandex.ru/images/search"
    params = {
        "text": query,
        "type": "photo",
        "max_files": num_images
    }

    response = requests.get(url, params = params)
    response.raise_for_status()
    os.makedirs(folder, exist_ok=True)
    soup = BeautifulSoup(response.text, 'html')
    links = soup.find_all('img',{'class': 'serp-item__thumb'})
    print(links)

    responseJson = response.json()

    for i, image_url in enumerate(response.json()["items"]):
         image_data = requests.get(image_url["preview"]).content
         file_name = str(i).zfill(4) + ".jpg"
         file_path = os.path.join(folder, file_name)
         with open(file_path, "wb") as file:
             file.write(image_data)
download_images("rose", "dataset/rose", 1000)
download_images("tulips", "dataset/tulips", 1000)