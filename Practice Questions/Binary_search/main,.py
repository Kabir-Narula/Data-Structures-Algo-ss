# works only sorted array and random access

def binary_search(my_list,key):
  lowest = 0
  highest = len(my_list) - 1
  
  while lowest <= highest:
    mid_index = (lowest + highest) // 2
    
    if key  == my_list[mid_index]:
      return f"{key} was found at index {mid_index}"
    elif key < my_list[mid_index]:
      highest = mid_index - 1
    else:
      lowest = mid_index + 1
  
  return -1