import logging
import socket
import unittest
from unittest.mock import patch, Mock

from libs.source import UrlSource

logging.disable(logging.CRITICAL)


class TestSource(unittest.TestCase):

    @patch('libs.source.urlopen')
    def test_url_source_read(self, mock_urlopen):
        mock_read = Mock()
        mock_read.read.return_value = b'Create empty bytes'
        a = Mock()
        a.__enter__ = Mock(return_value=mock_read)
        a.__exit__ = Mock(return_value=None)
        mock_urlopen.return_value = a

        obj = UrlSource(url='https://docs.python.org/3.7/whatsnew/3.7.html')
        text = obj.read()
        self.assertIsInstance(text, str)

    def test_url_source_read_bad_url(self):
        obj = UrlSource(url='https://docs.python.orgm')
        text = obj.read()
        self.assertIsNone(text)

    @patch('libs.source.urlopen')
    def test_url_source_read_timeout(self, mock_urlopen):
        mock_urlopen.side_effect = socket.timeout()

        obj = UrlSource(url='https://docs.python.orgm')
        text = obj.read()

        self.assertIsNone(text)
