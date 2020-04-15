import sys
import configargparse

from crawler import crawl_main
from finder import find_main


def get_parser():
    parser = configargparse.ArgumentParser(
        description='Openreview.net Crawling',
        formatter_class=configargparse.ArgumentDefaultsHelpFormatter)
    # Task dependent argument
    parser.add_argument('--base-url', type=str, default='https://openreview.net',
                        help='Base URL')
    parser.add_argument('--url', type=str, default='https://openreview.net/group?id=ICLR.cc/2020/Conference',
                        help='Target URL')
    parser.add_argument('--keyword', type=str, default='None',
                        help='Keyword you want to find')
    parser.add_argument('--mode', type=str, default='find',
                        help='crawl : get new crawl data\nfind : find the information using keyword')
    parser.add_argument('--dir', type=str, default='./',
                        help='Directory path for saving crawled data')

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.mode == 'crawl':
        crawl_main(args)
    elif args.mode == 'find':
        find_main(args)
    else:
        print('Invalid mode argument: ', args.mode)
        exit(0)
