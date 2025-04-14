class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start =0
        end = len(nums)
        if target in nums:
            while start <= end:
              mid = (start + end)//2
              if nums[mid] == target:
                return mid
              elif (target >nums[mid]):
                start = mid
              else:
                end = mid
        else:
            min_num = min(nums)
            max_num = max(nums)
            if target <min_num:
                return 0
            if target > max_num :
                return len(nums)
            while start <= end:
                mid = (start+end)//2
                if target > nums[mid]:
                    if nums[mid+1] > target:
                        return mid+1
                    start= mid
                else:
                    if nums[mid-1]< target:
                        return mid
                    end= mid
