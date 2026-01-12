# Last updated: 1/12/2026, 3:13:25 PM
class Solution:
    def compressedString(self, word: str) -> str:
        
        output = ""

        # while word
        while word:
            # get first char 
            char = word[0]
            count = 1
            # while next char and next char is same
            while count < len(word) and count < 9 and word[count] == char:
                # delete character and update count
                count += 1

            word = word[count:]
            # append output

            output += (str(count) + char)

        return output

        # 

        '''
        char = a
        count = 1
        word = bcde
        output = 1a
        '''