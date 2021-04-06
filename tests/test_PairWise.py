import unittest
from Pairwise import Pairwise

P = Pairwise()


class MyTestCase(unittest.TestCase):
    def test1(self):
        A = [6, 2, 3, 5, 6, 3]
        count = P.solution(A)

        self.assertEqual(count, 4)

    def test2(self):
        A = [1,2,1]
        count = P.solution(A)

        self.assertEqual(count, 2)

    def test3(self):
        A = [2,1,4,4]
        count = P.solution(A)

        self.assertEqual(count, 1)


if __name__ == '__main__':
    unittest.main()
