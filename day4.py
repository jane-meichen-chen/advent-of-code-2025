import os

from get_data import download_input_data

SURROUNDINGS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


if __name__ == "__main__":
    paper_rolls = [list(row) for row in download_input_data(4, os.environ["AUTH"]).split("\n")]
    lookup_map = {}
    for r, row in enumerate(paper_rolls):
        for c, paper_roll in enumerate(row):
            lookup_map[(c, r)] = paper_roll

    part_one = 0
    updated_map = lookup_map.copy()
    for (c, r), grid in lookup_map.items():
        if grid == "@" and sum(lookup_map.get((c+dc, r+dr), ".") == "@" for dc, dr in SURROUNDINGS) < 4:
            part_one += 1
            updated_map[(c, r)] = "."

    part_two = part_one
    while updated_map != lookup_map:
        lookup_map = updated_map.copy()
        for (c, r), grid in lookup_map.items():
            if grid == "@" and sum(lookup_map.get((c + dc, r + dr), ".") == "@" for dc, dr in SURROUNDINGS) < 4:
                part_two += 1
                updated_map[(c, r)] = "."

    print("part I: ", part_one)
    print("part II: ", part_two)
