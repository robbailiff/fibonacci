from argparse import ArgumentParser

def get_args() -> ArgumentParser:
    parser = ArgumentParser(description="Utility for parsing arguments")

    parser.add_argument("--num", type=int, default=20, help="The number in the sequence (optional, default is 20)")
    
    return parser.parse_args()