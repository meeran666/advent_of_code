import math
arr=[2,4,9,12,14]
left_pointer=0
right_pointer=len(arr)
targer=5
foundit=False
while(left_pointer!=right_pointer):
  mid=math.floor((right_pointer-left_pointer)/2)
  print(mid)
  if arr[mid]>targer:
    right_pointer=mid
  elif arr[mid]<targer:
    left_pointer=mid
  else:
    foundit=True
    break
print(foundit)