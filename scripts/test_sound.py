import sys
import os
import time
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from pages.page_sound import PageSound
from base.base_yml import get_data
import pytest


class TestSettings:

    def setup(self):
        self.driver = init_driver()
        self.page_sound = PageSound(self.driver)

    def test_gallium(self):
        self.page_sound.click_sound_and_inform()
        time.sleep(2)
        self.page_sound.click_default_sound()
        time.sleep(2)
        self.page_sound.click_gallium()

    def test_selenium(self):
        self.page_sound.click_sound_and_inform()
        time.sleep(2)
        self.page_sound.click_default_sound()
        time.sleep(2)
        self.page_sound.click_selenium()
