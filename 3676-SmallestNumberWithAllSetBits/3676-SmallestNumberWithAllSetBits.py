# Last updated: 1/12/2026, 3:12:59 PM
class Solution:
    def smallestNumber(self, n: int) -> int:
        
        # return smallest number >= where binary rep is only set bits
        # i.e. 1 + 2 + 4 + ...

        # probably want to start subtracting big powers of 2.
        # if we have to skip any, those are what we need to add to get to this number
        '''
        i = 0
        power = 0

        while i < n:
            i += 2 ** power

            power += 1

        return i
        '''

        # i think there is a way to figure this out

        # n < sum 2^x = 2^(x+1)-1

        # so n + 1 < 2^(x+1)
        # ceil log base 2 of (n+1) - 1 = x

        return 2 ** math.ceil(math.log(n+1, 2)) - 1

