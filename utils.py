import json
import datetime


def save_crawled_data(args, papers, name):
    timestamp = str(datetime.datetime.now())
    filename = args.dir + name + timestamp + '.json'

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent='\t')
