def solve(list1, list2):
  return ' '.join(
      map(str, set(list1).symmetric_difference(set(list2)))
  )


list1 = [1, 2,]
list2 = [1, 2, 3]
result = solve(list1, list2)
print(result)
