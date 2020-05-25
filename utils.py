import json
import datetime
import os
import re
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image
from collections import Counter



def save_crawled_data(args, papers, name):
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    filename = args.dir + name + timestamp + '.json'

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(papers, f, indent='\t')


def make_mask(icon_path):
    icon = Image.open(icon_path).convert("RGBA")
    mask = Image.new("RGB", icon.size, (255, 255, 255))
    mask.paste(icon, icon)
    mask = np.array(mask)

    return mask


def word_cloud(args):
    file_regex = r'(.*)_((\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})).json'
    files_dir = os.listdir(args.dir)
    files = []

    for file in enumerate(files_dir):
        files.append(file[1])

    crawled_date = re.search(file_regex, files[0]).group(2)
    keywords = []
    total_paper = 0

    for i in range(len(files)):
        dict = json.loads(open(args.dir + files[i], 'r').read())

        for j in range(len(dict)):
            temp = [x.strip() for x in dict[j]["Keywords:"].split(',')]
            temp = [x.lower() for x in temp]
            keywords += temp
            total_paper += 1

    word_cloud_dict = Counter(keywords)
    # plt_mask = np.array(Image.open("./mask.png"))
    plt_mask = make_mask("./mask.png")

    cloud = WordCloud(background_color='white', max_font_size=500, mask=plt_mask, max_words=1500, min_word_length=2)
    cloud.generate_from_frequencies(word_cloud_dict)

    tops = word_cloud_dict.most_common(args.tops)
    print("Total accepted paper: " + str(total_paper))
    print("\n*****Top-{} Keywords*****".format(args.tops))
    for i in range(args.tops):
        print(tops[i][0] + ': ' + str(tops[i][1]) + ' times')
    print("*" * 25)

    plt.figure(figsize=(20, 10))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    cloud.to_file('./' + crawled_date + '_result.png')
