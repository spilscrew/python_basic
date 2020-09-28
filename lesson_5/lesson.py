# pip install
# pip list
# pip freeze >requirements.txt
# pip install -r requirements.txt

import os
import requests
import lesson_5.functions


def get_html():
    _url = 'https://geekbrains.ru'
    _response = requests.get(_url)
    return _response.text


def save_html_to_file(_file_path, _html_text):
    with open(_file_path, 'w', encoding='UTF-8') as file:
        file.write(_html_text)


def save_image(_file_path, _img_bytes):
    with open(_file_path, 'wb') as file:
        file.write(_img_bytes)


def get_image(_url):
    _response = requests.get(_url)
    return _response.content


if __name__ == '__main__':
    img_url = 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/9558/retina-c94f3091e3c68919cbdfadb7c530d18e.png'
    file_name = 'temp_gb_main.html'
    file_folder = os.path.dirname(__file__)
    file_path = os.path.join(file_folder, file_name)
    image_path = os.path.join(file_folder, 'image.png')
    html_text = get_html()
    save_html_to_file(file_path, html_text)
    img_bytes = get_image(img_url)
    save_image(image_path, img_bytes)





# url = 'https://geekbrains.ru'
# response = requests.get(url)
# response_text = response.text
# print(response)
# print(response.text)
# print(os.name)
# print(os.environ)
# os.mkdir('test_mkdir')
# os.removedirs('test_mkdir')
# print(os.listdir())
# print(os.path.isdir('test_mkdir'))
# print(os.path.isfile('test_mkdir'))