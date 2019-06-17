from base.base_driver import init_driver
from page.page import Page

import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        print("hello")

    @pytest.mark.parametrize("keyword", ["xiaoming", "123", "hello"])
    def test_search(self, keyword):
        self.page.setting.click_search()
        self.page.search.input_search(keyword)
        self.page.search.click_back()
