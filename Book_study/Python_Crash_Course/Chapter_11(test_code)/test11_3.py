import unittest
from t11_3 import Employee


class TestEmployee(unittest.TestCase):
    """针对测试"""

    def setUp(self):
        """
        创建对默认增加的测试
        :return:
        """
        self.my_survey = Employee('xu', 'weicheng', 200)

    def test_no_rasis(self):
        self.result = self.my_survey.give_raise()
        self.assertEqual(self.result, 700)

    def test_raise(self):
        self.result = self.my_survey.give_raise(400)
        self.assertNotEqual(self.result, 700)
