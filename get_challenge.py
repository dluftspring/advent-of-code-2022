import requests
import os
import datetime

BASE_URL='https://adventofcode.com/2022/day/'

def get_input(day: int, session_cookie: str) -> None:
    """
    Get the challenge input from adventofcode.com
    """

    headers = {
        'cookie': session_cookie
    }

    response = requests.get(BASE_URL + f"{day}/input", headers=headers)
    assert response.status_code == 200, "Failed to get input"

    if not os.path.exists(f"day{day}/input"):
        os.makedirs(f"day{day}/input")

    with open(f"day{day}/input/input{day}.txt", "w") as f:
        f.write(response.text)

def get_puzzle(day: int, session_cookie: str) -> None:
    """
    Get the puzzle for the current calendar day
    """

    headers = {
        'cookie': session_cookie
    }

    response = requests.get(BASE_URL + f"{day}", headers=headers)
    assert response.status_code == 200, "Failed to get puzzle"

    if not os.path.exists(f"day{day}"):
        os.makedirs(f"day{day}")

    with open(f"day{day}/puzzle{day}.md", "w") as f:
        f.write(response.text)

def load_cookies() -> str:
    """
    Load the session cookie from a file
    """

    with open('secrets/cookie', 'r') as f:
        return f.read()

def get_calendar_day() -> int:
    """
    Return non zero padded calendar day of the year
    """
    return datetime.datetime.now().day

if __name__ == "__main__":
    get_puzzle(get_calendar_day(), load_cookies())
    get_input(get_calendar_day(), load_cookies())