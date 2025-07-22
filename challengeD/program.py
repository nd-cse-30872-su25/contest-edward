#!/usr/bin/env python3

import sys

def find_ways(num: int)-> tuple:
    if num < 2:
        return (0, None)
    dp = [set() for _ in range(num+1)]
    dp[2].add((2,))
    if num > 2:
        dp[3].add((3,))
    if num > 6:
        dp[7].add((7,))
    count = 4
    while count < num+1:
        for path in dp[count-2]:
            new_path = tuple(sorted(path + (2,)))
            dp[count].add(new_path)

        if count > 4:
            for path in dp[count-3]:
                new_path = tuple(sorted(path + (3,)))
                dp[count].add(new_path)

        if count > 6 and count != 7:
            for path in dp[count-7]:
                new_path = tuple(sorted(path + (7,)))
                dp[count].add(new_path)
        count+=1
    return(len(dp[num]), dp[num])

            

def main():
    for line in sys.stdin:
        num = int(line.strip())
        num_ways, ways = find_ways(num)
        if ways:
            ways = sorted(ways)
            if len(ways) == 1:
                print(f"There is 1 way to achieve a score of {num}:")
            else:
                print(f"There are {num_ways} ways to achieve a score of {num}:")
            for path in ways:
                path = map(str, path)
                print(" ".join(path))
        else:
            print(f"There are 0 ways to achieve a score of {num}:")
if __name__ == "__main__":
    main()
