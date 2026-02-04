import os

from get_data import download_input_data

if __name__ == "__main__":
    data = download_input_data(5, os.environ["AUTH"])
    ranges, ids = data.split("\n\n")

    ranges = list(map(lambda rg: tuple(map(int, rg.split("-"))), ranges.split("\n")))
    merged_ranges = []
    for start, end in sorted(ranges):
        if not merged_ranges:
            merged_ranges.append((start, end))
            continue
        prev_start, prev_end = merged_ranges.pop()
        if prev_end + 1 < start:
            merged_ranges += [(prev_start, prev_end), (start, end)]
        else:
            merged_ranges.append((min(prev_start, start), max(prev_end, end)))

    part_one = 0
    for fruit_id in ids.split("\n"):
        for start, end in merged_ranges:
            if start <= int(fruit_id) <= end:
                part_one += 1
                break
    print("part I: ", part_one)

    part_two = 0
    for start, end in merged_ranges:
        part_two += (end - start + 1)
    print("part II: ", part_two)
