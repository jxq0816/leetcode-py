class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rs=0
        size=len(height)
        for i in range(1,size-1):
            max_left=0
            max_right=0
            for j in range(i,-1,-1):
                max_left=max(height[j],max_left)
            for j in range(i,size):
                max_right=max(height[j],max_right)
            rs=rs+min(max_left,max_right)-height[i]
        return rs
if __name__ == '__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    solution=Solution()
    print(solution.trap(height))