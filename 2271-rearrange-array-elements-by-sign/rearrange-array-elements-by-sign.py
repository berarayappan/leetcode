class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos =[]
        neg = []
        ans = [0] * len(nums)
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        for i  in range(len(pos)):
            ans[2*i] = pos[i]
            ans[2*i +1] = neg[i]
        return ans        