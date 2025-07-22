#!/usr/bin/env python3

import sys

def find_operations(target: int)-> list:
    operations = ['']*8
    return perms(operations, 0, target)

def perms(operations: list, index: int, target: int)-> list:
    if index >= len(operations):
        return
    for i in range(index, len(operations)):
        operations[i] = "*"
        perms(operations, i+1, target)
        if eval(f"(((9 {operations[0]} 8) {operations[1]} 7) {operations[2]} 6) {operations[3]} (5 {operations[4]} (4 {operations[5]} (3 {operations[6]} (2 {operations[7]} 1))))") == target:
            break
        operations[i] = "+"
        perms(operations, i+1, target)
        if eval(f"(((9 {operations[0]} 8) {operations[1]} 7) {operations[2]} 6) {operations[3]} (5 {operations[4]} (4 {operations[5]} (3 {operations[6]} (2 {operations[7]} 1))))") == target:
            break
        operations[i] = "-"
        perms(operations, i+1, target)
        if eval(f"(((9 {operations[0]} 8) {operations[1]} 7) {operations[2]} 6) {operations[3]} (5 {operations[4]} (4 {operations[5]} (3 {operations[6]} (2 {operations[7]} 1))))") == target:
            break
    return operations


def main():
    for line in sys.stdin:
        line = int(line.strip())
        operations = find_operations(line)
        print(f"(((9 {operations[0]} 8) {operations[1]} 7) {operations[2]} 6) {operations[3]} (5 {operations[4]} (4 {operations[5]} (3 {operations[6]} (2 {operations[7]} 1)))) = {line}")

if __name__ == "__main__":
    main()
