import os

from get_data import download_input_data


def dial(current_value: int, instruction: str) -> int:
    diff = int(instruction[1:])
    if instruction.startswith("L"):
        diff = diff * -1
    new_value = current_value + diff
    while new_value < 0:
        new_value += 100
    return new_value % 100


if __name__ == "__main__":
    current_value = 50
    part_one = 0
    part_two = 0
    for instruction in download_input_data(1, os.environ["AUTH"]).split("\n"):
        if instruction:
            diff = int(instruction[1:])
            part_two += diff // 100
            if instruction.startswith("L"):
                new_value = current_value + (diff % 100) * -1
            else:
                new_value = current_value + (diff % 100)
            if new_value > 99 or (new_value <= 0 and current_value != 0):
                part_two += 1
            if new_value % 100 == 0:
                part_one += 1
            current_value = new_value % 100
    print("part I: ", part_one)
    print("part II: ", part_two)
