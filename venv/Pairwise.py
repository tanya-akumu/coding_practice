class Pairwise:
    def __init__(self):
        pass

    def solution(self,A):
        sorted_a = sorted(A)
        count = 0
        min_val = 1
        correct_arr = [i for i in range(1,len(A) + 1)]


        for i in range(len(sorted_a)):
            if count >= 1000000000:
                return -1
            else:
                count += (abs(sorted_a[i] - correct_arr[i]))


        return count