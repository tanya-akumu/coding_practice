import unittest
from CalculateTheSquare import CalculateTheSquare

C = CalculateTheSquare()


class MyTestCase(unittest.TestCase):
    def test_1(self):
        num_roots = C.solution(10,20)
        self.assertEqual(num_roots, 2)

    def test_2(self):
        num_roots = C.solution(6000,7000)
        self.assertEqual(num_roots, 3)

    def test_3(self):
        num_roots = C.solution(2,1000000000)
        print(num_roots)
        self.assertEqual(num_roots, 4)

    def test_4(self):
        num_roots = C.solution(7,428889083)
        print(num_roots)
        self.assertEqual(num_roots, 4)


if __name__ == '__main__':
    unittest.main()
