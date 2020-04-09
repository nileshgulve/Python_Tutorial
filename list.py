
x = 10
x
10

myname = 'nilesh gulve'
len(myname)
12

nums = [10,20,30,40]
nums
[10, 20, 30, 40]
nums[0]
10

nums[:-1]
[10, 20, 30]
nums[-1]
40
name = ['nilesh','saurabh','ashish','sai']
name
['nilesh', 'saurabh', 'ashish', 'sai']
name[:]
['nilesh', 'saurabh', 'ashish', 'sai']
name[:2]
['nilesh', 'saurabh']
name[0:]
['nilesh', 'saurabh', 'ashish', 'sai']
name[3:]
['sai']
values = [10.5,'nilesh',25]
values
[10.5, 'nilesh', 25]

#list store different type of data
mil = name + nums
mil
['nilesh', 'saurabh', 'ashish', 'sai', 10, 20, 30, 40]

nums.append(50)
name
['nilesh', 'saurabh', 'ashish', 'sai']
nums
[10, 20, 30, 40, 50]
# append at the append

nums.insert(2,60)
nums
[10, 20, 60, 30, 40, 50]

#pop delete element using index number
nums.pop(1)
20
nums
[10, 60, 30, 40, 50]
nums.pop()
50
del nums[2:]
nums
[10, 60]

#extend to add multiple values
nums.extend([12,15,80,90])
nums
[10, 60, 12, 15, 80, 90]
max(nums)
90
min(nums)
10
nums.sort()
nums
[10, 12, 15, 60, 80, 90]