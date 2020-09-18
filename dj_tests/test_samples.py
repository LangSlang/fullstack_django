from rest_framework.test import APITestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSamples(APITestCase):

    def test_one(self):
        two = 2
        self.assertEqual(2, two)
        self.assertNotEqual(1, two)

    def test_two(self):
        driver = webdriver.Firefox()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()