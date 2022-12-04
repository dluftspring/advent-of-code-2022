import os
import sys
import subprocess
import requests
import datetime

class AdventOfCodeClient(object):

    def __init__(self):
        self.session_cookie = self._get_session_cookie()

    def _get_session_cookie(self):
        with open('secrets/cookie', 'r') as f:
            return f.read()

    @property
    def base_url(self):
        return "https://adventofcode.com/2022"

    @property
    def http_headers(self):
        return {
            'cookie': self.session_cookie
        }

    def get_puzzle(self, day: int = datetime.datetime.now().day) -> None:
        response = requests.get(f"{self.base_url}/day/{day}", headers=self.http_headers)
        assert response.status_code == 200, "Failed to get puzzle"

        if not os.path.exists(f"day{day}"):
            os.makedirs(f"day{day}")

        with open(f"day{day}/puzzle{day}.md", "w") as f:
            f.write(response.text)

    def get_input(self, day: int = datetime.datetime.now().day) -> None:
        response = requests.get(f"{self.base_url}/day/{day}/input", headers=self.http_headers)
        assert response.status_code == 200, "Failed to get input"

        if not os.path.exists(f"day{day}/input"):
            os.makedirs(f"day{day}/input")

        with open(f"day{day}/input/input{day}.txt", "w") as f:
            f.write(response.text)

    def submit_response(self, day: int = datetime.datetime.now().day, part: int = 1) -> None:
        result = subprocess.run([sys.executable, "day" + str(day) + f"/day{str(day)}.py"], capture_output=True)
        assert result.returncode == 0, "Failed to run the day's script"

        guess_to_submit = result.stdout.decode('utf-8').split(' ')[-1].strip()
        print(f"Attempting to submit {guess_to_submit} for day {day}")

        response = requests.post(f"{self.base_url}/day/{day}/answer", headers=self.http_headers, data={
            "level": sys.argv[-1] or 1,
            "answer": guess_to_submit
        })
        assert response.status_code == 200, "Failed to submit response"

        print(self._process_response(response), flush=True)

    def _process_response(self, response: requests.Response) -> str:
        """
        Process response from advent of code and return the message of
        success or failure contained in the html tag
        """
        print(response, flush=True)