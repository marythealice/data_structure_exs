def sum_two_nums_equals_k(nums,k):
    nums.sort()
    left = 0
    right = (len(nums) - 1)
    result = [None, None]

    while left < right:
      sum = nums[left] + nums[right]
      if sum < k:
        left += 1
      elif sum > k:
        right -= 1
      else:
        result[0] = nums[left]
        result[1] = nums[right]
        break
    
    if result[0] == None:
      return []
    else:
      return result