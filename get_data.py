import requests


def download_input_data(day: int, cookie: str) -> str:
    url = f"https://adventofcode.com/2025/day/{day}/input"
    response = requests.get(url, headers={"Cookie": cookie})
    return response.text

