import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.s = Service(r"D:\Пары\chromedriver.exe")
        self.driver = webdriver.Chrome(r"D:\Пары\chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("1231")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def test_search_in_python_org_1(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
