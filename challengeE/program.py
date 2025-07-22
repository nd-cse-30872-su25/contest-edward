#!/usr/bin/env python3

import sys

def find_paths(tree: list, target)->list:
    paths = []
    _find_paths(tree, 0, [], 0, target, paths)
    return paths

def _find_paths(tree: list, index: int, path: list, curr_sum: int, target, paths: list)-> list:
    if index >= len(tree) or tree[index] == 0:
        return
     
    path.append(tree[index])
    curr_sum += tree[index]
    left = (2*index) + 1
    right = (2*index) + 2
    leaf = ((left >= len(tree) or tree[left] == 0) and (right >= len(tree) or tree[right] == 0))
    if curr_sum == target and leaf:
        paths.append(path.copy())
    else:
        _find_paths(tree, left, path, curr_sum, target, paths)
        _find_paths(tree, right, path, curr_sum, target, paths)
    curr = path.pop()
    curr_sum -= curr

def main():
    for line in sys.stdin:
        target = int(line.strip())
        tree = list(map(int, sys.stdin.readline().strip().split()))
        paths = find_paths(tree, target)
        paths = sorted(paths)
        if not paths:
            print(f"{target}:")
        else:
            for path in paths:
                print(f"{target}: {", ".join(map(str, path))}")
if __name__ == "__main__":
    main()
