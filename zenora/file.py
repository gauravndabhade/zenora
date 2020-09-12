import base64
from urllib.parse import urlparse
from .utils.helpers import get_file
import mimetypes
import urllib.parse
import os


class File:
    def __init__(self, url):
        file = get_file(url)
        path = url.split("?")
        encoded_body = base64.b64encode(file.content)
        print(encoded_body)
        self.data = "data:{};base64,{}".format(
            mimetypes.guess_type(path[0]), encoded_body.decode()
        )
