from argparse import ArgumentParser

def get_args() -> ArgumentParser:
    """Function for reading and parsing any command line arguments.

        --num[Optional]: The number in the fibonacci sequence. The default is 20.

    Returns:
        ArgumentParser: A namespace object holding attributes matching the args.
    """
    parser = ArgumentParser(description="Utility for parsing arguments")

    parser.add_argument("--num", type=int, default=20, help="The number in the sequence (optional, default is 20)")
    
    return parser.parse_args()