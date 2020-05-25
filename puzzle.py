def show(s):
  for row in s:
    for c in row:
      print(c,end=" ")
    print()
  print()

def pos0(s):
  for r in range(3):
    for c in range(3):
      if s[r][c] == 0:
        return r, c

def swap(s, r, c):
  new = [[e for e in row] for row in s]
  row, col = pos0(new)
  new[row][col] = new[row+r][col+c]
  new[row+r][col+c] = 0
  return new

def move(s, x):
  if x=='u':
    return swap(s,-1,0)
  elif x=='d':
    return swap(s,1,0)
  elif x=='l':
    return swap(s,0,-1)
  elif x=='r':
    return swap(s,0,1)

def actions(s):
  row, col  = pos0(s)
  actions = []
  if row > 0:
    actions += 'u'
  if row < 2:
    actions += 'd'
  if col > 0:
    actions += 'l'
  if col < 2:
    actions += 'r'
  return actions

def myHash(s):
  return ''.join([str(e) 
      for row in s 
      for e in row])

def bfs(instate, finstate):
  visited, queue = [], [instate]
  path = {myHash(instate): []}
  while queue:
    s = queue.pop(0) # DFS: queue.pop(-1)
    if s == finstate:
      return path[myHash(finstate)]
    if s not in visited:
      visited.append(s)
      for a in actions(s):
        nextstate = move(s,a)
        queue.append(nextstate)
        h = myHash(nextstate)
        if h not in path:
          path[h] = [s
            for s in path[myHash(s)]]
          path[h].append(a)

if __name__ == "__main__":
    instate = [[1,2,3],[0,5,6],[4,7,8]]
    finstate = [[1,2,3],[4,5,6],[7,8,0]]
    res = bfs(instate,finstate)
    print(res)
    s = instate
    show(s)
    for a in res:
      s = move(s,a)
      show(s)

    

