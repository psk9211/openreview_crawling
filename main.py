import sys
import configargparse

import utils
from crawler import crawl_main


def get_parser():
    parser = configargparse.ArgumentParser(
        description='Openreview.net Crawling',
        formatter_class=configargparse.ArgumentDefaultsHelpFormatter)
    # Task dependent argument
    parser.add_argument('--base-url', type=str, default='https://openreview.net',
                        help='Base URL')
    parser.add_argument('--url', type=str, default='https://openreview.net/group?id=ICLR.cc/2020/Conference',
                        help='Target URL')
    # parser.add_argument('--keyword', type=str, default='None',
    #                     help='Keyword you want to find')
    parser.add_argument('--mode', type=str, default='cloud',
                        help='crawl : get new crawl data\nfind : find the information using keyword')
    parser.add_argument('--dir', type=str, default='./data/',
                        help='Directory path for saving crawled data')
    parser.add_argument('--tops', type=int, default=20,
                        help="The number of keywords")

    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.mode == 'crawl':
        posters, spotlights, talks = crawl_main(args)
        print('Saving crawled data...')
        utils.save_crawled_data(args, papers=posters, name='poster_')
        utils.save_crawled_data(args, papers=spotlights, name='spot_lights_')
        utils.save_crawled_data(args, papers=talks, name='talk_')
        # print('Done.')
        print('Crawling complete!')

    elif args.mode == 'cloud':
        # print('Word Cloud Visualization')
        utils.word_cloud(args)
        # print('end')

    else:
        print('Invalid argument: ' + args.mode + ', exiting...')
        exit()
