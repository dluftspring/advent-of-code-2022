from common.client import AdventOfCodeClient

def main():
    client = AdventOfCodeClient()
    client.get_puzzle()
    client.get_input()

if __name__ == "__main__":
    main()