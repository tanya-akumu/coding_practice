import unittest
from NTimesN import NTimesN

N = NTimesN()


class MyTestCase(unittest.TestCase):
    def test1(self):
        A = [3, 8, 2, 3, 3, 2]
        max_val = N.solution(A)
        self.assertEqual(max_val, 3)

    def test2(self):
        A = [7, 1, 2, 8, 2]
        max_val = N.solution(A)
        self.assertEqual(max_val, 2)

    def test3(self):
        A = [3, 8, 2, 3, 3, 2]
        max_val = N.solution(A)
        self.assertEqual(max_val, 3)

    def test4(self):
        A = [5, 5, 5, 5, 5]
        max_val = N.solution(A)
        self.assertEqual(max_val, 5)

    def test4(self):
        A = [1]
        max_val = N.solution(A)
        self.assertEqual(max_val, 1)

    def test5(self):
        A = [1,1,3,4,5,6,7,8,9,10]
        max_val = N.solution(A)
        self.assertEqual(max_val, 0)

    def test6(self):
        A = [1,2,3,4,5,6,7,8,9,10]
        max_val = N.solution(A)
        self.assertEqual(max_val, 1)

    def test7(self):
        A = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8]
        max_val = N.solution(A)
        self.assertEqual(max_val, 8)


if __name__ == '__main__':
    unittest.main()
