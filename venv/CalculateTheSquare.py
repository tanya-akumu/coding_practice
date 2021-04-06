class CalculateTheSquare:
    def __init__(self):
        pass

    def solution(self,A,B):
        num_roots = 0
        num = 2
        square = num**2

        while square <=B:
            num_roots += 1
            num  = square
            square = num ** 2

        return num_roots

