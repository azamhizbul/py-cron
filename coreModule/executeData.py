

import requests, json
import urllib.request
from PIL import Image


def uploadImage():
    urllib.request.urlretrieve(
    'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
    "tmpImage/gfg.png")
    Image.open("tmpImage/gfg.png")
    url = 'http://localhost:3000/uploadImage'
    files = [
        ('image',('tmpImage/gfg.png',open('tmpImage/gfg.png','rb'),'image/png'))
    ]
    headers={}
    payload={}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.json()


