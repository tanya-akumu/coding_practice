from unittest import TestCase
from RoadRoller import RoadRoller
from random import randint

class Test(TestCase):

    def test_solution(self):
        R = RoadRoller()

        x_1 = [2, 4, 2, 6, 7, 1]
        y_1 = [0, 5, 3, 2, 1, 5]
        w_1 = 2

        x_2 = [4, 8, 2, 2, 1, 4]
        y_2 = [1, 2, 3, 1, 2, 3]
        w_2 = 3

        x_3 = [0, 3, 6, 5]
        y_3 = [0, 3, 2, 4]
        w_3 = 1

        drives_1 = R.solution(x_1, y_1, w_1)
        self.assertEqual(drives_1, 3)
        R.num_drives = 1

        drives_2 = R.solution(x_2, y_2, w_2)
        self.assertEqual(drives_2, 2)
        R.num_drives = 1

        drives_3 = R.solution(x_3, y_3, w_3)
        self.assertEqual(drives_3, 3)

    def test_solution_one(self):
        R = RoadRoller()

        x = [2]
        y = [0]
        w = 2

        drives_3 = R.solution(x, y, w)
        self.assertEqual(drives_3, 1)
