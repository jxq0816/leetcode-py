class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or len(height)==0:
            return 0

        size=len(height)
        left_max=[[0]*size for i in range(size)]
        right_max=[[0]*size for i in range(size)]
        left_max[0]=height[0]
        right_max[size - 1] = height[size - 1]
        for i in range(1,size):
            left_max[i] = max(height[i], left_max[i - 1])
        rs = 0
        for i in range(size-2,-1,-1):
            right_max[i]=max(height[i],right_max[i+1])

        for i in range(1,size-1):
            tmp=min(left_max[i],right_max[i])-height[i]
            if tmp>0:
                rs=rs+tmp
        return rs

if __name__ == '__main__':
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    solution=Solution()
    print(solution.trap(height))