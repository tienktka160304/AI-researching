# Input: arr[] = [1, 2, 3, 5]
# Output: 4
# Explanation: All the numbers from 1 to 5 are present except 4.
class Solution:
    def missingNum(self, arr):
        # code here
        l = len(arr) + 1
        sum_total = (l + 1) * l // 2
        missing_sum = sum(arr)
        return (sum_total - missing_sum)
