from django.shortcuts import render

# Create your views here.
def mode(req, n):
    nums = n.split(',')
    nums = [int(num) for num in nums]
    nums.sort()
    length = len(nums)
    mode = 0
    max_count = 0
    current_count = 0
    current_num = nums[0]
    for i in range(length):
        if nums[i] == current_num:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = current_num
            current_count = 1
            current_num = nums[i]
    if current_count > max_count:
        mode = current_num
    return render(req, 'mode.html', {'mode': mode, 'freq': max_count})