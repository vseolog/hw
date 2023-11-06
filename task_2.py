data = input('Enter string: ',)

def perm(data):
  if len(data) == 1:
    return data
  perm_list = []
  data = list(data)
  for elem in data:
    remaining_elements = [i for i in data if i != elem]
    iter = perm(remaining_elements)
    for j in iter:
      perm_list.append([elem]+list(j))
  return perm_list

pre_ans = perm(data)
for i in pre_ans:
  ans = ''
  for j in i:
    ans +=j
  print(ans)
