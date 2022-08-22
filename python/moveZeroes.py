def moveZeroes(nums):
        count = 0;
        nums1 = []
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums1.append(nums[i])
            else:
                count += 1
        for i in range(count):
            nums1.append(0)
        print(nums1)

moveZeroes([0,1,0,3,12])
