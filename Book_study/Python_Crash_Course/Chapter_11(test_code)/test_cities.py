import unittest
from city_functions import place


class NameTestCase(unittest.TestCase):
    """测试"""

    def test_place(self):
        place2 = place('beijing', 'china', 500000)
        self.assertEqual(place2, 'Beijing,China - population 500000')


unittest.main()