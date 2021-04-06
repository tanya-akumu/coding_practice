import unittest
from DiverseWord import  DiverseWord

D = DiverseWord()


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        # word = DiverseWord()
        A = 6; B = 1; C = 1
        new_string = D.solution(A,B,C)
        print(new_string)
        self.assertEqual(new_string, "aabaacaa" or "aacaabaa")


if __name__ == '__main__':
    unittest.main()
