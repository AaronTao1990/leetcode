class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        pass

    def findMedian(self, array):
        pass

    def findKth(self, array, k):
        pivot = 0
        n = self.partition(array, 0, len(array)-1, pivot)
        if n == k:
            return array[n]

    def partition(self, array, left, right, pivot):
        pivot_v = array[pivot]
        array[pivot], array[right] = array[right], array[pivot]
        cur_idx = left
        for i in range(left, right):
            if array[i] < pivot_v:
                array[cur_idx], array[i] = array[i], array[cur_idx]
                cur_idx = cur_idx + 1
        array[cur_idx], array[right] = array[right], array[cur_idx]
        return cur_idx

    def merge(self, nums1, nums2):
        i = j = 0
        nums = []
        while i<len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i = i + 1
            else:
                nums.append(nums2[j])
                j = j + 1

        for i in range(i, len(nums1)):
            nums.append(nums1[i])

        for j in range(j, len(nums2)):
            nums.append(nums2[j])

        return nums

#def test_partition():
#    array = [5, 3, 6, 7, 2]
#    partition(array, 0, len(array)-1, 2)
#    print array
#
#def test_merge():
#    array1 = [2, 5, 6, 9]
#    array2 = [1, 3, 4, 8]
#    array = merge(array1, array2)
#    print array

def main():
    solution = Solution()
    num1 = [1, 4, 5]
    num2 = [2, 3, 6]
    solution.findMedianSortedArrays(num1, num2)

if __name__ == '__main__':
    main()
