# Last updated: 1/12/2026, 3:13:21 PM
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if red == 1 and blue == 1:
            return 1
        
        # start with red and then do the same for blue
        layer = 1
        tempred = red
        tempblue = blue
        while((red>=0 and blue>=0) or (tempred>=0 and tempblue>=0) ):
            if layer%2==0:
                red-=layer
                tempblue-=layer
            else:
                blue-=layer
                tempred-=layer
            layer+=1
        
        return layer-2