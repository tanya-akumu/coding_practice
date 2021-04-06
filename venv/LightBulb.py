class LightBulb:
    def __init__(self):
        pass

    def solution(self,A):
        sorted_a = sorted(A)
        pref_sum_a = self.prefix_sum(A)
        pref_sum_sort = self.prefix_sum(sorted_a)
        shine_count = 0

        for i in range(len(A)):
            if pref_sum_sort[i] == pref_sum_a[i]:
                shine_count += 1

        return shine_count

    def prefix_sum(self,A):
        pref_sum = [A[0]]*len(A)

        for i in range(1,len(A)):
            pref_sum[i] = pref_sum[i-1] + A[i]

        return pref_sum
