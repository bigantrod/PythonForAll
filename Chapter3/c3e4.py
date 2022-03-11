from ast import Or #Needed for a potential change to if statement

nums = [1, 2, 1]  # Change numbers in array to evaluate if number are same or different.
# nums = input(nums)
print('test')
if nums[0] == nums[1]:
    print('They are all the same')
elif nums[1] != nums[2]:
    print('They are the same')
# Easier way format.

if nums[1] == nums[2]:
    print('They are all the same')
elif nums[1] != nums[0]:
    print('They are not the same')
print('The End')
