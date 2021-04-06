class DiverseWord:

    def __init__(self):
        pass

    def solution(self,A, B, C):
     # write your code in Python 3.6

      result = ''
      count_a = A
      count_b = B
      count_c = C

      while count_a != 0 or count_b != 0 or count_c != 0:

         if count_a > 0:
             result,count_a = self.append_string(result,'a',count_a)

         if count_b > 0:
             result,count_b = self.append_string(result,'b',count_b)

         if count_c > 0:
             result,count_c = self.append_string(result,'c',count_c)

      print("Final result ",result)
      return result

    def append_string(self,string,letter, count):

        index = self.get_insert_index(string,letter)

        if index == -1:
            count = 0

        else:

            if count > 1:
                # if index == 0:
                #     string += letter*2
                #     count -= 2
                # else:
                string = string[:index] + letter*2 + string[index:]
                count -= 2
            else:
                # if index == 0:
                #     string += letter
                #     count -= 1
                # else:
                string = string[:index] + letter + string[index:]
                count -= 1

        return string,count

    def get_insert_index(self,string,letter):

        index = len(string)
        if string == '' or index == 1:
            index = 0
        else:

            last_val = string[-1]
            second_last_val = string[-2]
            if last_val != second_last_val and last_val != letter:# and second_last_val != letter:
                index = string.index(last_val)+1
            elif last_val == letter and second_last_val and len(string) > 2:
                index = -1
            else:
                # index = 0
                index = len(string)

        return index


if __name__ == '__main__':
    A = 6
    B = 1
    C = 1
    str_builder = DiverseWord()
    new_string = str_builder.solution(A, B, C)
    a2 = 1; b2 = 3; c2 = 1
    new_string = str_builder.solution(a2, b2, c2)
    a3 = 0; b3 = 1; c3 = 8
    new_string = str_builder.solution(a3, b3, c3)
    # print(new_string)
