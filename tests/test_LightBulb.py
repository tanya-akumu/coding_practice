import unittest
from LightBulb import LightBulb

L = LightBulb()

class MyTestCase(unittest.TestCase):
    def test_1(self):
        A = [2,1,3,5,4]
        shine_count = L.solution(A)
        self.assertEqual(shine_count, 3)

    def test_2(self):
        A = [2, 3, 4, 1, 5]
        shine_count = L.solution(A)
        self.assertEqual(shine_count, 2)

    def test_3(self):
        A = [1, 3, 4, 2, 5]
        shine_count = L.solution(A)
        self.assertEqual(shine_count, 3)

    def test_4(self):
        A = [i for i in range(1,100001)]
        shine_count =L.solution(A)
        self.assertEqual(shine_count,100000)


if __name__ == '__main__':
    unittest.main()
