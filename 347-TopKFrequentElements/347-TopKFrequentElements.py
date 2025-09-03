# Last updated: 9/2/2025, 11:00:58 PM
class Solution(object):
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in sort[:k]]

