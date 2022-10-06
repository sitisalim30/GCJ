def three_d_printing():
  cartridges = [list(map(int, input().split())) for _ in range(3)]
  result = []
  cnt = D
  for j in range(4):
    c = min(min(cartridges[i][j] for i in range(len(cartridges))), cnt)
    result.append(c)
    cnt -= c
  return " ".join(map(str, result)) if cnt == 0 else "IMPOSSIBLE"

D = 10**6
for case in range(int(input())):
  print('Case #%d: %s' % (case+1, three_d_printing()))
