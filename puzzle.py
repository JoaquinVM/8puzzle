def show(s):
  print('-------------')
  for row in s:
    print('| '+ ' | '.join([str(i) for i in row]) +' |')
    print('-------------')

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
  if x=='arriba':
    return swap(s,-1,0)
  elif x=='abajo':
    return swap(s,1,0)
  elif x=='izquierda':
    return swap(s,0,-1)
  elif x=='derecha':
    return swap(s,0,1)

def actions(s):
  row, col  = pos0(s)
  actions = []
  if row > 0:
    actions.append('arriba')
  if row < 2:
    actions.append('abajo')
  if col > 0:
    actions.append('izquierda')
  if col < 2:
    actions.append('derecha')
  return actions

def myHash(s):
  return ''.join([str(e) 
      for row in s 
      for e in row])

def bfs(instate, finstate):
  visited, queue = [], [instate]
  path = {myHash(instate): []}
  while queue:
    s = queue.pop(0)
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
            for s in path[myHash( s)]]
          path[h].append(a)

def to_nums(inp):
  return [int(x) for x in inp.strip().split(' ')]

if __name__ == "__main__":
    print('Ingrese estado inicial')
    inputI1 = input('Fila 1(ej: 1 2 3 ): ')
    inputI2 = input('Fila 2: ')
    inputI3 = input('Fila 3: ')
    print('Ingrese estado final')
    inputF1 = input('Fila 1: ')
    inputF2 = input('Fila 2: ')
    inputF3 = input('Fila 3: ')
    
    instate = [to_nums(inputI1), 
                to_nums(inputI2),
                to_nums(inputI3)]
    finstate = [to_nums(inputF1), 
                to_nums(inputF2),
                to_nums(inputF3)]

    res = bfs(instate,finstate)
    print('Solucion: ', res)
    s = instate
    show(s)
    for a in res:
      s = move(s,a)
      show(s)

    

