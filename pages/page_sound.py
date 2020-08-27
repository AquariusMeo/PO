from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageSound(BaseAction):

    sound_and_inform_button = By.XPATH, "text,提示音和通知"
    default_sound_button = By.XPATH, "text,默认通知铃声"
    gallium_button = By.XPATH, "text,Gallium,1"
    selenium_button = By.XPATH, "text,Selenium,1"

    def click_sound_and_inform(self):
        self.click(PageSound.sound_and_inform_button)

    def click_default_sound(self):
        self.click(PageSound.default_sound_button)

    def click_gallium(self):
        self.click(PageSound.gallium_button)

    def click_selenium(self):
        self.click(PageSound.selenium_button)
