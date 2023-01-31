from collections import deque
import re

def prod(list):
    b = list[0]
    for i in range(1, len(list), 1):
        b *= list[i]
    return b


def sum_func(list):
    return sum(list)


def subtraction(list):
    b = list[0]
    for i in range(1, len(list), 1):
            b -= list[i]
    return b


def division(list):
    b = list[0]
    for i in range(1, len(list), 1):
        b //= list[i]
    return b


nums_queue = deque([x for x in input().split()])
curr_nums = []

while len(nums_queue) > 0:
    curr = nums_queue.popleft()
    if re.search(r"[-]?\d", str(curr)):
        curr_nums.append(int(curr))
    elif curr == '+':
        nums_queue.appendleft(sum_func(curr_nums))
        curr_nums.clear()
    elif curr == '*':
        nums_queue.appendleft(prod(curr_nums))
        curr_nums.clear()
    elif curr == '-':
        nums_queue.appendleft(subtraction(curr_nums))
        curr_nums.clear()
    elif curr == '/':
        nums_queue.appendleft(division(curr_nums))
        curr_nums.clear()

print(curr_nums[0])
