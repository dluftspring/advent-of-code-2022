from get_challenge import get_calendar_day
from get_challenge import load_cookies
import requests
import sys
import subprocess

def submit_challenge(day: int, session_cookie: str) -> None:

    headers = {
        'cookie': session_cookie
    }

    result = subprocess.run([sys.executable, "day" + str(day) + f"/day{str(day)}.py"], capture_output=True)
    assert result.returncode == 0, "Failed to run the day's script"

    guess_to_submit = result.stdout.decode('utf-8').split(' ')[-1].strip()
    print(f"Attempting to submit {guess_to_submit} for day {day}")

    response = requests.post(f"https://adventofcode.com/2022/day/{day}/answer", headers=headers, data={'level': 2, 'answer': guess_to_submit})
    assert response.status_code == 200, "Failed to submit answer"

    print(response.text)


def process_response(response: requests.Response) -> str:
    """
    Process the response from the website and return a human readable status
    """
    pass


if __name__ == "__main__":
    submit_challenge(get_calendar_day(), load_cookies())