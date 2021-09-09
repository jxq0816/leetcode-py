class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
        for key, value in dict.items():
            print(str(key)+"出现了"+str(value)+"次")

if __name__ == '__main__':
    array=[2,2,3,2]
    solution=Solution()
    print(solution.singleNumber(array))