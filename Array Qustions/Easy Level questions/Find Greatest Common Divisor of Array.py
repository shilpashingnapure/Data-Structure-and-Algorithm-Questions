'''
Find Greatest Common Divisor of Array
Easy


Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
'''

def findGCD(nums) -> int:
	mn = min(nums)
	mx = max(nums)
	largest_gcd = 0
	for i in range(1,mx+1):
		if mn % i == 0 and mx % i == 0:
			largest_gcd = max(largest_gcd , i)
	return largest_gcd
print(findGCD([2,5,6,9,10]))