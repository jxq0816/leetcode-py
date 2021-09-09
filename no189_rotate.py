class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        t=[]
        j=0
        for i in range(n-k,n):
            t.insert(j,nums[i])
            j=j+1

        for i in range(k-1,n)[::-1]:
            nums[i]=nums[i-k]

        for i in range(0,k):
            nums[i]=t[i]

if __name__ == '__main__':
    array=[1,2,3,4]
    solution=Solution()
    n=len(array)
    solution.rotate(array,2)
    for i in range(0,n):
        print(array[i])