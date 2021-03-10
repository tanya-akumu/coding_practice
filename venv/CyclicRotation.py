def solution(A, K):
    '''
    Shifts elemens of an array A by a value K. If the
    shift overflows the length of the array, the element
    is placed in such a way that it cycles around the array.
    The algorithm is as follows:
    1. Create a copy of array A filled with invalid elements
    2. Set condition to return the array if the length of
    the array is 1 or the value to shift by is 0 or the length
    of the array
    3. Loop through each element of the array:
       - compute the value by which each element is to
       be shifted by
       - compute the new index by setting it as the remainder
       of the shifting value divided by the length of the array
       - copy the current element into the new index at the copy
       array

    Performance in terms of correctness and efficiency is 100%
    
    :param A: (int) Array of int elements to be movec
    :param K: (int) Value to move elements by
    :return: (Array) Array of elements shifted by K
    '''
    # write your code in Python 3.6
    arr_len = len(A)
    copy_a = [1001] * arr_len

    if not A or arr_len == 1 or K == 0 or K == arr_len:return A

    for i in range(arr_len):
        num_moves = i + K
        index = num_moves % arr_len

        copy_a[index] = A[i]

    return copy_a