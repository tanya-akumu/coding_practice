import unittest
from CountBalloon import CountBalloon

count_balloon = CountBalloon()


class MyTestCase(unittest.TestCase):

    def test_1(self):
        word = 'BAONXXOLL'
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 1)

    def test_2(self):
        word = 'BAOOLLNNOLOLGBAX'
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 2)

    def test_3(self):
        word = 'QAWABAWONL'
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 0)

    def test_4(self):
        word = 'ONLABLABLOON'
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 1)

    def test_5(self):
        word = 'B'
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 0)

    def test_6(self):
        word_arr = ['B', 'A', 'L', 'L', 'O', 'O', 'N'] * 28000
        word_arr += (['X', 'P', 'K', 'D'] * 1000)
        word = ''.join(word_arr)
        moves = count_balloon.solution(word)
        self.assertEqual(moves, 28000)


if __name__ == '__main__':
    unittest.main()
