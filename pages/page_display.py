from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageDisplay(BaseAction):

    display_button = By.XPATH, "text,显示"
    search_button = By.ID, "com.android.settings:id/search"
    text_input_area = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_display(self):
        self.click(PageDisplay.display_button)

    def click_search(self):
        self.click(PageDisplay.search_button)

    def input_text_in_search(self, text):
        self.input_text(PageDisplay.text_input_area, text)

    def click_back(self):
        self.click(PageDisplay.back_button)
