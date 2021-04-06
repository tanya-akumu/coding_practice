class NTimesN:
    def __init__(self):
        pass

    def solution(self,A):
        max_val = 0
        count = 1
        sorted_a = sorted(A)

        if sorted_a.count(sorted_a[0]) == len(A):
            return sorted_a[0]

        for i in range(len(A)-1):
            val1 = sorted_a[i]
            val2 = sorted_a[i+1]
            if val1 == val2:
                count +=1
            elif count == val1:
                if max_val < val1:
                    max_val = val1
                count = 1

        if count == val2 and max_val < val2:
                max_val = val2

        return max_val

