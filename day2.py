import os

from get_data import download_input_data


def find_invalid_nums(num_range: str) -> list[int]:
    invalid_nums = []
    start, end = tuple(map(int, num_range.split("-")))
    num = start
    while num < end + 1:
        num_str = str(num)
        if len(num_str) % 2 != 0:
            num_part = "1" + "0" * (len(num_str) // 2)
            num = int(num_part + num_part)
        else:
            mid = len(num_str) // 2
            if num_str[:mid] == num_str[mid:]:
                invalid_nums.append(num)
            num += 1
    return invalid_nums


def find_more_invalid_nums(num_range: str) -> list[int]:
    invalid_nums = []
    start, end = tuple(map(int, num_range.split("-")))
    for num in range(start, end + 1):
        num_str = str(num)
        if (num_str + num_str).find(num_str, 1) < len(num_str):
            invalid_nums.append(num)
    return invalid_nums


if __name__ == "__main__":
    part_one = 0
    part_two = 0
    for num_range in download_input_data(2, os.environ["AUTH"]).split(","):
        part_one += sum(find_invalid_nums(num_range))
        part_two += sum(find_more_invalid_nums(num_range))
    print("part I: ", part_one)
    print("part II: ", part_two)
