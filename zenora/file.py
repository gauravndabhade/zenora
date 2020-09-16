import base64
from urllib.parse import urlparse
from .utils.helpers import get_file
import mimetypes


class File:
    """File object for sending file data to Discord in data URI scheme"""

    def __init__(self, url):
        file = get_file(url)
        path = url.split("?")
        encoded_body = base64.b64encode(file.content)
        self.data = "data:{};base64,{}".format(
            mimetypes.guess_type(path[0]), encoded_body.decode()
        )
