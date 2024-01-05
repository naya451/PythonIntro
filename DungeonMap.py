from collections import defaultdict, deque
import sys

def can_reach_exit(tunnels, entrance, exit):
    graph = defaultdict(list)
    for tunnel in tunnels:
        cave1, cave2 = tunnel.split()
        graph[cave1].append(cave2)
        graph[cave2].append(cave1)

    visited = set()
    queue = deque([entrance])

    while queue:
        current_cave = queue.popleft()
        if current_cave == exit:
            return "YES"
        visited.add(current_cave)
        for neighbor in graph[current_cave]:
            if neighbor not in visited:
                queue.append(neighbor)

    return "NO"

inp = []
for s in sys.stdin:
    inp.append(s)

tunnels = inp[:len(inp) - 2]
entrance = inp[-2].replace('\n', '')
ext = inp[-1].replace('\n', '')
tunnels = [x.replace('\n', '') for x in tunnels]

print(can_reach_exit(tunnels, entrance, ext))
