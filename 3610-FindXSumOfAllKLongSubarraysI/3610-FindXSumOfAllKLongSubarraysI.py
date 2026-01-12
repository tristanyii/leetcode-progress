# Last updated: 1/12/2026, 3:13:08 PM
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def topXElements():
            print(numCount.items())
            srt = sorted(numCount.items(), key=lambda x: (x[1],x[0]), reverse = True)
            # print(srt)
            #srt = sorted(numCount.items(), key=lambda x: x[1], reverse = False)
            # print(srt)

            if len(srt) < x:
                return srt

            # print(srt[:x])
            # print("\n")
            return srt[:x]

        def calcSum(srt):
            subSum = 0

            for i in range(len(srt)):
                subSum += srt[i][0] * srt[i][1]

            return subSum
        
        n = len(nums)
        answer = []
        l = 0
        r = k - 1

        numCount = collections.defaultdict(int)

        currSum = 0
        for i in range(l, k):
            if i >= len(nums):
                break

            numCount[nums[i]] += 1

        # currSum = sum(topXElements())
        # answer.append(currSum)

        while r < len(nums):
            
            # currSum = sum(topXElements()[0])
            currSum = calcSum(topXElements())
            answer.append(currSum)
            # print("append answer: ", currSum)

            numCount[nums[l]] -= 1
            l += 1

            r += 1
            if r < len(nums):
                numCount[nums[r]] +=1 
        

        return answer
              
           



# NOTES
# - sum of top x most frequent elements in array
# - Size of each subarray: static
#     - == k
# - Number of subarrays: n - k + 1
# - sliding window
#     - l = 0, r = k
