from rest_framework.test import APITestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSamples(APITestCase):

    def test_one(self):
        two = 2
        self.assertEqual(2, two)
        self.assertNotEqual(1, two)
