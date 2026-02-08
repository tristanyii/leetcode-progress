# Last updated: 2/7/2026, 11:26:36 PM
1class Solution:
2    def fizzBuzz(self, n: int) -> List[str]:
3        res = []
4        for n in range(1, n + 1):
5            if n % 3 == 0 and n % 5 == 0:
6                res.append("FizzBuzz")
7            elif n % 3 == 0:
8                res.append("Fizz")
9            elif n % 5 == 0:
10                res.append("Buzz")
11            else:
12                res.append(str(n))
13        return res