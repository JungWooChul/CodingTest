class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        start, end = 0, len(height) - 1
        while(start != end):
            if height[start] < height[end]:
                if water < self.calWater(start, end, height[start]):
                    water = self.calWater(start, end, height[start])
                start += 1
            else:
                if water < self.calWater(start, end, height[end]):
                    water = self.calWater(start, end, height[end])
                end -= 1
        return water
    
    def calWater(self, start, end, height):
        return (end-start) * height