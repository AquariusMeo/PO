import sys
import os
import time
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from pages.page_display import PageDisplay
from base.base_yml import get_data
import pytest


class TestSettings:

    def setup(self):
        self.driver = init_driver()
        self.page_display = PageDisplay(self.driver)

    @pytest.mark.parametrize('text', get_data('data_display')['test_input_in_display'])
    def test_input_in_display(self, text):
        self.page_display.click_display()
        time.sleep(2)
        self.page_display.click_search()
        time.sleep(2)
        self.page_display.input_text_in_search(text)
        time.sleep(2)
        self.page_display.click_back()
