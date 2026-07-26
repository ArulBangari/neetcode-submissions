class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_arr = []
        for i1 in range(len(nums)):
            difference_dict = defaultdict(list)
            for i2 in range(i1 + 1, len(nums)):
                if nums[i2] in difference_dict:
                    for pair in difference_dict[nums[i2]]:
                        add = pair + [nums[i2]]
                        check = True
                        
                        for ret_arr in return_arr:
                            if self.compareTuple(ret_arr, add):
                                check = False
                        
                        if check:
                            return_arr.append(add)


                difference_dict[-1*(nums[i1] + nums[i2])].append([nums[i1], nums[i2]])
        return return_arr

    def compareTuple(self, nums1, nums2):
        if nums1[0] in nums2 and nums1[1] in nums2:
            return True
        return False