class OddOccurrences:

    def __init__(self):
        pass

    def solution(self,A):
        '''
        Finds the unpaired element in the array A.
        :param A: (Array of ints)
        :return:(int) value of unpaired element
        '''
        # write your code in Python 3.6

        sorted_a = sorted(A)
        count = 1
        # print(sorted_a)
        if len(A) == 1:
            return A[- 1]

        for i in range(len(sorted_a)):
            #stopping case 1 (odd occurence at the end of array)
            if i == len(sorted_a) - 1 and count == 1:
                return sorted_a[-1]
            else:
                val1 = sorted_a[i]
                val2 = sorted_a[i + 1]

                if val1 == val2:
                    count +=1
                else:
                    if count % 2 == 0:
                        # print(f"The value: {val1} appears {count} times")
                        count = 1
                    else:
                        # print(f"The value: {val1} appears 1 times")
                        return val1