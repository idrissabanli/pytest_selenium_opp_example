from selenium import webdriver
import pytest

class TestGoogle():

    @pytest.fixture
    def setUp_tearDown(self):
        self.browser_driver = webdriver.Firefox(executable_path='/home/idris/PythonProjects/python_oop/geckodriver')
        self.browser_driver.get('https://www.google.com/')
        yield
        self.browser_driver.close()

    def test_title(self, setUp_tearDown):
        expected_page_title = 'Google'
        actual_page_title = self.browser_driver.title
        assert expected_page_title == actual_page_title
    
    def test_input(self, setUp_tearDown):
        self.browser_driver.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

    



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