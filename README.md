# Advent of Code 2022

This repo contains my solutions to the [Advent of Code 2022](https://adventofcode.com/2022) challenges.

## Quickstart

Install poetry. Ideally with pipx but regular pip will work just fine

```bash
pipx install poetry
```

Install dependencies

```bash
poetry install
```

Activate the venv

```bash
poetry shell
```

You'll also have to get your session cookies from the browser and place them in a file called `cookie` in the
secrets/ directory. This is used to authenticate with the Advent of Code site since all input files are slightly different.

## Getting input data

The input data for each day's challenge is stored in a file named `input.txt` in the corresponding day's directory.
To get the input data for a given day, run the following command from the root directory:

```bash
python3 get_challenge.py
```

You should then see the following file in a directory named after the current calendar day of the month

day${day}/inputs/input.txt

Happy coding!

## Submitting a response

TODO