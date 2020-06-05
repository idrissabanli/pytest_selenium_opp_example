from selenium import webdriver
from unittest import TestCase

class TestGoogle(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser_driver = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        cls.browser_driver.get('https://www.google.com/')

    def test_title(self):
        expected_page_title = 'Google'
        actual_page_title = self.browser_driver.title
        assert expected_page_title == actual_page_title
    
    def test_input(self):
        self.browser_driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

    @classmethod
    def tearDownClass(cls):
        cls.browser_driver.close()
        



# def test_title():
#     browser_driver = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
#     browser_driver.get('https://www.google.com/')
#     expected_page_title = 'Google'
#     actual_page_title = browser_driver.title
#     assert expected_page_title == actual_page_title
#     browser_driver.close()

# def test_input():
#     browser_driver = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
#     browser_driver.get('https://www.google.com/')
#     browser_driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
#     browser_driver.close()