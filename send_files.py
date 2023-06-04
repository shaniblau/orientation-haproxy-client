import os

import requests


def upload_file():
    url = 'http://20.185.67.127:8000/uploadfile'
    files = create_files("../dogs")
    server = requests.post(url, files=files)
    output = server.text
    print('The response from the server is:\n', output)


def create_files(directory: str):
    files: list = []
    files_names: list = os.listdir(directory)
    for name in files_names:
        file_path = os.path.join(directory, name)
        files.append(('files', (name, open(file_path, 'rb'), 'image/jpeg')))
    return files


