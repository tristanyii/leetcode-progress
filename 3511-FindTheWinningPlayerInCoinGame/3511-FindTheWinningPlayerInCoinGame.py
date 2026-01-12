# Last updated: 1/12/2026, 3:13:14 PM
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        return "Bob" if int(min(x,y/4))%2==0 else "Alice"