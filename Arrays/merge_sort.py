def merge_sort(a, b):
  if len(a) == 0 or len(b) == 0:
    return a + b

  sortlist=[]
  i = 0
  j = 0
  while i < len(a) and j < len(b):
    print(sortlist)

    if a[i] <= b[j]:
      sortlist.append(a[i])
      i += 1

    elif b[j] < a[i]:
      sortlist.append(b[j])
      j += 1

  return sortlist + a[i:] + b[j:]

a = []
b = [2, 3, 4, 5, 6, 9, 11, 76]
x = merge_sort(a, b)
print(x)