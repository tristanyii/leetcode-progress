# Last updated: 3/14/2026, 2:47:47 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        left = 0
4        fruit_counter = defaultdict(int)
5        max_fruit = 0
6
7        for right in range(len(fruits)):
8            fruit_counter[fruits[right]] += 1
9
10            while len(fruit_counter) > 2:
11                fruit_counter[fruits[left]] -= 1
12
13                if fruit_counter[fruits[left]] == 0:
14                    del fruit_counter[fruits[left]]
15                left += 1
16            
17            max_fruit = max(max_fruit, right - left + 1)
18
19        return max_fruit
20        