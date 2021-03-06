from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def click(self, button):
        self.find_element(button).click()

    def input_text(self, area, text):
        self.find_element(area).send_keys(text)

    def find_element(self, loc):
        loc_by = loc[0]
        loc_value = loc[1]
        if loc_by == By.XPATH:
            loc_value = self.make_xpath(loc_value)
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(loc_by, loc_value))

    @staticmethod
    def make_xpath_mid(expr):
        alist = expr.split(',')
        if len(alist) == 2:
            xpath_mid = "contains(@" + alist[0] + ",'" + alist[1] + "')"
        elif (len(alist) == 3) and alist[2] == '0':
            xpath_mid = "contains(@" + alist[0] + ",'" + alist[1] + "')"
        elif (len(alist) == 3) and alist[2] == '1':
            xpath_mid = "@" + alist[0] + "='" + alist[1] + "'"
        else:
            raise Exception("XPATH expression not correct.")
        return xpath_mid + 'and '

    def make_xpath(self, expr):
        xpath_start = '//*['
        xpath_end = ']'
        xpath_mid = ''
        if isinstance(expr, str):
            if expr.startswith("//*["):
                return expr
            xpath_mid = self.make_xpath_mid(expr).rstrip('and ')
        elif isinstance(expr, list):
            for i in expr:
                xpath_mid += self.make_xpath_mid(i)
            xpath_mid = xpath_mid.rstrip('and ')
        else:
            raise TypeError("XPATH expression must be a string or a list.")
        return xpath_start + xpath_mid + xpath_end
