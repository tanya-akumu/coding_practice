class GenomicRange:
    def __init__(self):
        pass

    def solution(self,S,P,Q):
        # create prefix sums for A,C,G and T
        # loop through P:
        # find if A is in selection : sum[Q] - sum[P-1] > 0