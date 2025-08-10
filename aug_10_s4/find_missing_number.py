"""
Find missing number from 0 to N
No duplicates

Different approaches
1. Check all numbers and see which is missing O(N^2)
2. Sort Check if next number is current - 1 O(NlogN)
3. Sum of n numbers - Sum of given array O(N)
4. XOR of full arr with given arr O(N)

"""
def find_missing_number_2(nums: list) -> int:
     nums.sort()
     for i in range(len(nums)-1):
          if nums[i+1] - nums[i] != 1:
               return nums[i]+1


def find_missing_number_3(nums: list) -> int:
        if 0 not in nums:
            return 0
        total = len(nums)+1
        total_sum = ( total * (total-1) ) // 2 
        return total_sum - sum(nums)

def find_missing_number_4(nums: list) -> int:
    full_nums = range(0,len(nums)+1)
    y=full_nums[0]
    for i in full_nums[1:]:
        y = y ^ i
    x=nums[0]
    for i in nums[1:]:
        x = x ^ i
    return x ^ y


if __name__ == "__main__":
    print(find_missing_number_2([0,1,2,3,4,5,6,7,9]))
    print(find_missing_number_3([0,1,2,3,4,5,6,7,9]))
    print(find_missing_number_4([0,1,2,3,4,5,6,7,9]))