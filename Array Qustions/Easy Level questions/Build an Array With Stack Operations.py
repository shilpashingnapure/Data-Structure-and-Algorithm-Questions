'''
Build an Array With Stack Operations
Easy

Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
'''

def buildArray(target, n: int):
	arr = list(range(1 , n+1))
	ans = []
	for i in arr:
		if max(target) >= i:
			ans.append("Push")
			if i not in target:
				ans.append("Pop")
	return ans
print(buildArray([1,3] , 3))