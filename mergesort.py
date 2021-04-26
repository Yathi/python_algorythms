

def sort(arr):
  lo = 0
  hi = len(arr) - 1
  mid = (hi + lo)//2

  if hi > 0:
    lower = sort(arr[lo:mid+1])
    higher = sort(arr[mid+1:hi+1])
    return merge(lower, higher)
  else:
    return [arr[0]]

def merge(first, second):
  i,j = 0, 0
  result = []
  iWall = len(first)
  jWall = len(second)

  for k in range(iWall + jWall):
    if i == iWall:
      result.append(second[j])
      j += 1
    elif j == jWall:
      result.append(first[i])
      i += 1
    elif first[i] <= second[j]:
      result.append(first[i])
      i += 1
    else:
      result.append(second[j])
      j += 1

  return result

print(sort([2, 1, 3, 7, 7, 2, 5, 34, 9]))
#print(sort([2, 1]))
