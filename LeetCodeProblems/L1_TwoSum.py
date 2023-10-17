class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        array = self.nums
        value = self.target
        output = []
        i = 0
        j = len(array)-1
        sum = -10000
        while sum != value:
            num1 = array[i]
            num2 = array[j]
            temp = 0
            if i < j:
                temp = num1+num2
                if temp == value:
                    sum = temp
                    output.append(i)
                    output.append(j)
                else:
                    j = j-1
            else:
                if i==j:
                    i = i+1
                    j = len(array)-1

        print(output)
x = (input())
y = int(input())
char = x.split()
nums = []
for num in char:
    nums.append(int(num))

Sol = Solution(nums, y)
Sol.twoSum()