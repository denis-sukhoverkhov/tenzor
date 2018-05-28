import logging
import unittest

from bs4 import Tag, BeautifulSoup

from libs.text_analyzer import Strategy, LongTextStrategy

logging.disable(logging.CRITICAL)


class TestTextAnalyzer(unittest.TestCase):

    def test_html_dom_to_flat_div(self):
        html = "<div>привет, <div>мир</div>. Сегодня день был хороший <div><p>и вчера был такой же</p>" \
               "<p>и вчера был такой же</p><p>p text 2</p><p>p text 3</p></div> да</div>"
        tag_list = Strategy._html_dom_to_flat_div(html)
        self.assertIsInstance(tag_list, list)

    def test_find_post(self):
        html = "<div>привет, <div>мир</div>. Сегодня день был хороший <div><p>и вчера был такой же</p>" \
               "<p>и вчера был такой же</p><p>p text 2</p><p>p text 3</p></div> да</div>"
        strategy = LongTextStrategy(html)
        post = strategy.algorithm_interface()
        self.assertIsInstance(post, Tag)
        new_post = str(post)
        self.assertEqual(new_post, '<div><p>и вчера был такой же</p><p>и вчера был '
                                   'такой же</p><p>p text 2</p><p>p text 3</p></div>')

    def test_modify_links(self):
        a_text1 = 'text__1'
        a_text2 = 'text__2'
        soup = BeautifulSoup(f"<div><a href='text.html'>{a_text1}</a> и <a href='text2.html'>{a_text2}</a></div>")
        new_soup = Strategy._modify_link(soup)
        new_soup = str(new_soup)
        self.assertFalse(a_text1 in new_soup)
        self.assertFalse(a_text2 in new_soup)
        self.assertFalse('<a href=' in new_soup)
        self.assertTrue('[text.html]' in new_soup)
        self.assertTrue('[text2.html]' in new_soup)

    def test_replace_p_h_space(self):
        soup = BeautifulSoup(f"<div><h3>title<h3><p>ptext1</p> и <p>ptext2</p></div>")
        new_soup = Strategy._replace_p_h_new_line(soup)
        new_soup = str(new_soup)
        self.assertTrue('title\n' in new_soup)
        self.assertTrue('ptext1\n' in new_soup)
        self.assertTrue('ptext2\n' in new_soup)
