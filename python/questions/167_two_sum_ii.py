# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Example:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None
        # dic = {}
        # for i, num in enumerate(numbers):
        #     if target-num in dic:
        #         return [dic[target-num]+1, i+1]
        #     dic[num] = i

        for i in range(0, len(numbers)):
            difference = target - numbers[i]
            if difference in numbers and i != numbers.index(difference):
                return[i+1, numbers.index(difference)+1]


if __name__ == '__main__':
    input = [2,7,11,15]
    target = 13
    print(Solution.twoSum(0, input, target))
