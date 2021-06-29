input_ = int(input())

edges = list()

def hanoi_sol(n, from_, to, other, edges):
    if n == 1:
        edges.append((from_, to))
        return
    
    hanoi_sol(n-1, from_, other, to, edges)
    edges.append((from_, to))
    hanoi_sol(n-1, other, to, from_, edges)

hanoi_sol(input_, 1, 3, 2, edges)

print(len(edges))
for (i, j) in edges:
    print(i, j)    
        

# for insert mode
