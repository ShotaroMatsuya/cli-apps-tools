#!/usr/local/bin/python

import argparse
import random
import data

# Color
from termcolor import cprint

# Usage
# randomix --recommend movies/books/blog
# randomix --recommend movies/books/blog --limit 5


# Data
# books_list = ["Bible", "Unscripted", "Vision is not enough", "10x"]


def main():
    """A Simple Recommendation CLI"""
    parser = argparse.ArgumentParser(description="Randomix: A Simple Recommendation CLI", prog="randomix", epilog="Recommendation by Randomization")

    # Version
    parser.add_argument('--version', '-v', version='%(prog)s 0.01', action='version', help='Version Info')
    
    # Optional Argument
    parser.add_argument('--recommend', '-r', help='Randomly Recommend', choices=['books', 'movies', 'datascience'])
    parser.add_argument('--limit', '-l', help="Set Limit", default=2, type=int)
    
    # Namespace
    args = parser.parse_args()
    print(args)
    # colored(TEXT, fg,bg,attr=[])
    
    if args.recommend == 'books':
        cprint("Recommended {}".format(args.recommend), 'white', 'on_blue')
        results = random.choices(data.books_list, k=args.limit)
        for result in results:
            print(result)
    elif args.recommend == 'movies':
        cprint("Recommended {}".format(args.recommend), 'white', 'on_blue')
        results = random.choices(data.movies_list, k=args.limit)
        for result in results:
            print(result)
    elif args.recommend == 'datascience':
        cprint("Recommended {}".format(args.recommend), 'white', 'on_blue')
        results = random.choices(data.datascience_blogs, k=args.limit)
        for result in results:
            print(result)
    else:
        cprint("Recommended {}".format(args.recommend), 'white', 'on_blue')
        results = random.choices(data.books_list, k=args.limit)
        for result in results:
            print(result)


if __name__ == '__main__':
    main()
