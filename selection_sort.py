def find_smallest(arr):
  """find min in array"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
  
def selection_sort(arr):
  """append in new array"""
  new_arr = []
  for i in range(len(arr)):
      smallest = find_smallest(arr)
      new_arr.append(arr.pop(smallest))
  return new_arr
