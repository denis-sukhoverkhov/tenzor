import logging
import socket
from urllib.error import URLError
from urllib.request import urlopen
from abc import ABC, abstractmethod


class ISource(ABC):

    @abstractmethod
    def read(self) -> str:
        pass


class UrlSource(ISource):

    def __init__(self, url: str):
        self.url = url

    def read(self):
        html_str = None
        try:
            with urlopen(self.url) as response:
                html_bin = response.read()
                html_str = html_bin.decode('utf-8')
        except URLError as e:
            logging.warning(e)
        except socket.timeout as e:
            logging.warning(e)

        return html_str
