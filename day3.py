import os

from get_data import download_input_data


def get_joltage(battery_bank: str, digits = 2) -> int:
    joltage = 0
    starting_index = 0
    for i in range(digits):
        current_number = "0"
        new_starting_index = starting_index
        for pos, num in enumerate(battery_bank[starting_index:len(battery_bank)-(digits - i - 1)]):
            if num > current_number:
                current_number = num
                new_starting_index = starting_index + pos
        joltage = joltage * 10 + int(current_number)
        starting_index = new_starting_index + 1
    return joltage


if __name__ == "__main__":
    part_one = 0
    part_two = 0
    for row in download_input_data(3, os.environ["AUTH"]).split("\n"):
        part_one += get_joltage(row)
        part_two += get_joltage(row, digits=12)
    print("part I: ", part_one)
    print("part II: ", part_two)
