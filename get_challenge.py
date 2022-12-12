from common.client import AdventOfCodeClient
import sys

def main():
    client = AdventOfCodeClient()
    day = sys.argv[-1]
    client.get_puzzle(day=day)
    client.get_input(day=day)

if __name__ == "__main__":
    main()