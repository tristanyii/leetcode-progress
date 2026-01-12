# Last updated: 1/12/2026, 3:13:16 PM
class Solution:
    def maxOperations(self, s: str) -> int:

        # start from the left

        output = 0
        one_stack = 0
        first_zero = False

        # loop over the numbers
        for char in s:

            # we want to know the collections of ones.
            # they will move together
            if char == '1':
                first_zero = True
                one_stack += 1

            # when we get to a zero, how many ones did we just have stacked?
            elif first_zero:
                first_zero = False
                output += one_stack

            # when we get to the next 1, restart the count and add the last stacked ones
            # to the output

        return output
                

            




                
    