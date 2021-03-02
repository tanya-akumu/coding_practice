from random import randint
import time

class RoadRoller:

    def __init__(self):
        self.num_drives = 1

    def solution(self, X, Y, W) -> int:
        """
        :param X:
        :type W: int
        """
        # sort X
        # choose first index as starting point
        # get x + W
        # check if subsequent values of x are < x + W
        # pop values from the list
        # increment counter if value in x array is greater than x + W
        # select new starting point
        # repeat

        if X:
            sorted_X = sorted(X)
            # arr_len = len(sorted_X)
            # num_drives = 1

            while len(sorted_X) != 0:
                start = sorted_X[0]
                width = start + W

                for i in range(len(sorted_X)):
                    x = sorted_X[0]
                    if x >= start and x <= width:
                        sorted_X.pop(0)
                    else:
                        self.num_drives += 1
                        # start = sorted_X[0]
                        # width = start + W
                        break
        else:
            self.num_drives = 0

        return self.num_drives

    def solution2(self,X, Y, W):
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
    print(f"First solution executed in: {t2-t1:0.4f} seconds")
    t3 = time.perf_counter()
    drives = r.solution2(x, y, w)
    t4 = time.perf_counter()
    print(f"second solution executed in: {t4-t3:0.4f} seconds")

    print("Number of drives: ", drives)

