def unique_str(s):
  count = {}
  for i in s:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1

  for k,v in count.items():
    if v > 1:
      return False
  return True


def is_permutation(s1, s2):
  if not len(s1) == len(s2):
    return False
  s1 = ''.join(sorted(s1))
  s2 = ''.join(sorted(s2))

  return s1 == s2

def urlify(s,c):
  s = s.replace(" ", '%20')

