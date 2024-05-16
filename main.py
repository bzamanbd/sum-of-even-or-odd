def sum_of_even(nums:list[int]):
    total:int = 0
    for num in nums:
        if (num % 2 ) ==0:
            total += num
    print(f"Total is {total}") 

sum_of_even([1,2,3,4,5,6])

