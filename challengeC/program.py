#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        num = int(line.strip())
        missing_ops(num)

if __name__ =="__main__":
    main()
