import textwrap
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup, Tag
from copy import copy


class TextAnalyzer:

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        self._strategy.algorithm_interface()


class Strategy(ABC):

    @abstractmethod
    def algorithm_interface(self):
        pass

    @staticmethod
    def _html_dom_to_flat_div(text):
        """
        Оставляет только div-ы с текстом,
        :param text:
        :return:
        """
        soup = BeautifulSoup(text)
        container = soup.find("div")

        div_list = [n for n in container.descendants]

        return div_list

    @staticmethod
    def _modify_link(soup: Tag):
        soup_l = copy(soup)
        for a in soup_l.find_all('a'):
            a.parent.insert(a.parent.index(a), f"[{a['href']}]")
            a.contents = []
            a.unwrap()

        return soup_l

    @staticmethod
    def _replace_p_h_new_line(soup: Tag):
        """
        Заменяет теги p и h на перенос строки
        :param soup:
        :return:
        """
        soup_l = copy(soup)
        for p in soup_l.find_all(['p', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            p.parent.insert(p.parent.index(p)+1, "\n")
            p.unwrap()

        return soup_l

    @staticmethod
    def _format_text_width(text: str, width: int):
        return textwrap.fill(text, width)


class LongTextStrategy(Strategy):

    def __init__(self, text):
        self.text = text

    def algorithm_interface(self):
        tag_list = self._html_dom_to_flat_div(self.text)

        max_len = 0
        post = None
        for idx, tag in enumerate(tag_list):
            if isinstance(tag, Tag):
                text = tag.get_text()
                current_len = len(text)
                if current_len > max_len:
                    post = tag
                    max_len = current_len

        return post
