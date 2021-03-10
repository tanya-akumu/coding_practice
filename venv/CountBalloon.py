class CountBalloon:

    def __init__(self):
        pass

    def solution(self, S):
        '''
        This problem removes the letters in 'BALLOON in a single move
        and counts how many moves are required to remove the group of
        letters in a string
        input: S (string) - string to be checked
        output: max_moves (int) - number of times the group of letters
        are removed in a string
        '''
        balloon_dict = {'B':1,'A':1,'L':2,'O':2,'N':1}
        max_moves = 0

        for letter in S:

            if letter == 'B' and balloon_dict['B'] != 0:
                balloon_dict['B'] -= 1
            elif letter == 'A' and balloon_dict['A'] != 0:
                balloon_dict['A'] -= 1
            elif letter == 'L' and balloon_dict['L'] != 0:
                balloon_dict['L'] -= 1
            elif letter == 'O' and balloon_dict['O'] != 0:
                balloon_dict['O'] -= 1
            elif letter == 'N' and balloon_dict['N'] != 0:
                    balloon_dict['N'] -= 1

            if balloon_dict['B'] == 0 and balloon_dict['A'] == 0 and balloon_dict['L'] == 0 and balloon_dict['O'] == 0\
                    and balloon_dict['N'] == 0:
                max_moves += 1
                balloon_dict['B'] = 1
                balloon_dict['A'] = 1
                balloon_dict['L'] = 2
                balloon_dict['O'] = 2
                balloon_dict['N'] = 1

        return max_moves