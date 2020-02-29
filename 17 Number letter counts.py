from num2words import num2words

nums = ""
for i in range(1, 1001):
    nums += num2words(i)
nums = nums.replace("-", "")
nums = nums.replace(" ", "")
print(nums)
print(len(nums))
