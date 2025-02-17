def find_product_execept_self(nums):
    product_array = []
    left = 1

    for i in range(len(nums)):
        current_product = 1
        for num in nums[i+1:]:
            current_product *= num
        
        product_array.append(current_product*left)

        left *= nums[i]
    
    return product_array