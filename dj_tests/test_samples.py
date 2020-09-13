from rest_framework.test import APITestCase

class TestSamples(APITestCase):

    def test_one(self):
        two = 2
        self.assertEqual(2, two)
        self.assertNotEqual(1, two)
