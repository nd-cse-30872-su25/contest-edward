#!/usr/bin/env python3

import sys

def find_buildings(buildings : list)->int:
    curr_max = -sys.maxsize - 1
    if buildings:
        count = 0
    else:
        return 0
    for building in reversed(buildings):
        if building > curr_max:
            count +=1
            curr_max = building
    return count

def main():
    for line in sys.stdin:
        line = list(map(int, line.strip().split()))
        building = find_buildings(line)
        print(building)


if __name__ == "__main__":
    main()
