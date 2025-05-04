# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash_map = dict()
        
        for index, val in enumerate(nums): # duyệt từng phần tử trong nums và index của nó
            if val in hash_map: # nếu val trong hash_map -> có số trước đó (= target - val)
                return [hash_map.get(val), index]

            hash_map[target - val] = index # nếu chưa thấy val -> Lưu phần bù (target - val) vào hash_map + lưu index hiện tại
        return []