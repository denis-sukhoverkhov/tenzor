import logging
import os
import shutil
import unittest

from libs.repository import FileRepository

logging.disable(logging.CRITICAL)


class TestRepository(unittest.TestCase):

    def setUp(self):
        super(TestRepository, self).setUp()

        self.abs_path = os.path.join(os.getcwd(), 'libs')
        self.path_to_temp = os.path.join(self.abs_path, 'tests', 'temp')

        if os.path.exists(self.path_to_temp):
            shutil.rmtree(self.path_to_temp)

        os.makedirs(self.path_to_temp)

    def tearDown(self):
        shutil.rmtree(self.path_to_temp)

    def test_file_repository_save(self):
        path = os.path.join(self.path_to_temp, 'lenta.ru', 'news', '2013', '03', 'dtp', 'index.txt')
        obj = FileRepository(content='example', path=path)
        self.assertTrue(obj.save())
        self.assertTrue(os.path.exists(path))
