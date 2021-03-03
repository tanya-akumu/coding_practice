from random import randint
import time

class RoadRoller:

    def __init__(self):
        pass

    def solution(self,X, Y, W):
        '''
        Solution for finding minimum number of drives required to patch
        all potholes on a road from a random starting point (x,0). The
        algorithm is as follows:
        1. Sort the x cordinates array in ascending order.
        2. Pick lowest x value as start point. This is to ensure all
        potholes will be patched.
        3. Get the width frame that the road roller can patch in a single drive
        4. Iterate through x coordinates:
            - if the value of x is within the width frame, continue
            - else
                - increment number of drives
                - set x as new start point
                - compute the new widthframe

        :param X: (array ints) x coordinates of potholes
        :param Y: (array ints) y coordinates of potholes
        :param W: (int) width of the roadroller
        :return: drives (int) number of drives needed to patch potholes
        '''
        sorted_X = sorted(X)
        start = sorted_X[0]
        width = start + W
        num_drives = 1

        for i,x in enumerate(sorted_X):
            if x >= start and x <= width:
                continue
            else:
                num_drives += 1
                start = x
                width = start + W

        return num_drives


if __name__ == '__main__':

    x = [randint(0, 1000000000) for i in range(100000)]
    y = [randint(0, 1000000000) for i in range(100000)]
    w = randint(1, 1000000000)
    r = RoadRoller()
    t1 = time.perf_counter()
    drives = r.solution(x, y, w)
    t2 = time.perf_counter()
    print(f"Solution executed in: {t2-t1:0.4f} seconds")
    print("Number of drives: ", drives)

