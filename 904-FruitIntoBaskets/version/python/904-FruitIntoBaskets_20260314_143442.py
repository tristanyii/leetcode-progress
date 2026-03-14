# Last updated: 3/14/2026, 2:34:42 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        left = 0
4        fruitCount = defaultdict(int)
5        maxFruit = 0
6
7        for right in range(len(fruits)):
8            fruitCount[fruits[right]] += 1
9            while len(fruitCount) > 2:
10                fruitCount[fruits[left]] -= 1
11
12                if fruitCount[fruits[left]] == 0:
13                    del fruitCount[fruits[left]]
14                left += 1
15                
16            maxFruit = max(maxFruit, right - left + 1)
17        return maxFruit
18            
19
20
21
22        