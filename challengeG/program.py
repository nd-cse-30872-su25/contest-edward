#!/usr/bin/env python3
import sys
from collections import deque

def dfs(graph: list, start: int, total_visited: set()) -> tuple:
    frontier = deque([start])
    visited = set()

    while frontier:
        curr = frontier.pop()
        if curr in visited:
            continue
        visited.add(curr)
        total_visited.add(curr)
        for index, neighbor in enumerate(graph[curr]):
            if neighbor == 1:
                frontier.append(index)
    visited = list(visited)
    visited.sort()
    return tuple(visited)

def main():
    system_num = 1
    for line in sys.stdin:
        chips = int(line.strip())
        count  = 0
        graph = []
        while count < chips:
            curr_line = list(map(int, sys.stdin.readline().strip().split()))
            graph.append(curr_line)
            count +=1
        visited = set()
        total_visited = set()
        for i in range(len(graph)):
            if i in total_visited:
                continue
            curr = dfs(graph, i, total_visited)
            visited.add(curr)
        circuits = len(visited)
        print(f"System {system_num} isolated circuits: {circuits}")
        system_num+=1
if __name__ == "__main__":
    main()
