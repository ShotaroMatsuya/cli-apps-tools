import argparse


def main():
    """A Simple CLI with Argparse"""
    # Constructor/Init
    parser = argparse.ArgumentParser(prog="basiccli", description="A simple cli with argparse", epilog="Additional Description")

    # Version
    parser.add_argument('--version', '-v', version='%(prog)s 0.01', action='version')

    args = parser.parse_args()
    
    
if __name__ == '__main__':
    main()