# Last updated: 1/12/2026, 3:13:40 PM
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if a == b == c:
            return "equilateral"
        if (
            a + b > c
            and b + c > a
            and a + c > b
        ):
            if a == b or a == c or b == c:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"


# # NOTES
# - can form triangle if:
#     a + b > c
#     b + c > a
#     a + c > b