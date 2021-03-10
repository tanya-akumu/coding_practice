def solution(N):
    '''
    Computes the length of the longest binary gap of an
    integer. A binary gap is determined by the number of
    0s in between 1s in the binary equivalent of an integer.
    The algorithm is as follows:
    1. Convert interger to binary equivalent
    2. Convert it to list
    3. Set the largest binary gap len to 0
    4. Set the zero counter to 0
    5. Loop through each element and count the number of
    0s in between the 1 digits.
    6. If the binary gap is less than the current zero
    count, set the zero count as the new binary length

    Performance and correctness score:100%
    :param N: (int) integer to compute binary gap
    :return: (int) length of the longest binary gap
    '''
    # write your code in Python 3.6
    n_bin = bin(N)[2:]
    n_bin_lst = list(n_bin)
    bg_len = 0
    z_count = 0

    # print("bin value of N is: ",n_bin)

    for i,digit in enumerate(n_bin_lst):

        if digit == '1' and z_count > 0:
            if bg_len < z_count:
                bg_len = z_count
            z_count = 0
        elif digit == '0': 
            z_count += 1

    return bg_len