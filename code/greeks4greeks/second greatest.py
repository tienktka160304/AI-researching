# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        sorting_arr = sorted(set(arr))
        if len(sorting_arr) > 1:
            return sorting_arr[len(sorting_arr) - 2]
        else:
            return -1
