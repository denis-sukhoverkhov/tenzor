import logging
import socket
from urllib.error import URLError
from urllib.request import urlopen
from abc import ABC, abstractmethod

import os


class IRepository(ABC):

    @abstractmethod
    def save(self) -> bool:
        pass


class FileRepository(IRepository):

    def __init__(self, content: str, path: str):
        self.content = content
        self.path = path

    def save(self) -> bool:
        try:
            dir_name = os.path.dirname(self.path)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open(self.path, 'w') as f_in:
                f_in.write(self.content)
        except Exception as e:
            logging.warning(e)
            return False

        return True
