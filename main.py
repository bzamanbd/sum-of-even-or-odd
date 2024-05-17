def sum_of_even_odd(nums:list):
    total:int = 0
    for num in nums:
        # if (num % 2) == 0:
        if (num % 2) != 0:
            total += num
    # print(f"The total of evens is {total}")
    print(f"The total of odds is {total}")

sum_of_even_odd([1,2,3,4,5,6,7,8,9])