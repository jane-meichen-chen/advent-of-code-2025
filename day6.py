import math
import os
import re
from typing import Iterable

from get_data import download_input_data


def calculate(operator: str, nums: Iterable[int]) -> int:
    if operator == "*":
        return math.prod(nums)
    else:
        return sum(nums)


if __name__ == "__main__":
    data = download_input_data(6, os.environ["AUTH"])

    nums = zip(*[re.split(r"\s+", row.strip()) for row in data.split("\n")[:-1]])
    operators = data.split("\n")[-1]

    part_one = sum(calculate(op, num) for num, op in zip(nums, re.split(r"\s+", operators)))
    print("part I: ", part_one)

    part_two = 0
    data_rows = data.split("\n")[:-1]
    nums = []
    op = ""
    for i in range(len(data.split("\n")[0])):
        if operators[i] != " ":
            if op:
                part_two += calculate(op, nums)
            nums = []
            op = operators[i]

        num = 0
        for j in range(len(data_rows)):
            if data_rows[j][i] != " ":
                num = num * 10 + int(data_rows[j][i])
        if num > 0:
            nums.append(num)

    part_two += calculate(op, nums)
    print("part II: ", part_two)
