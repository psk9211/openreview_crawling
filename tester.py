import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://openreview.net/group?id=ICLR.cc/2020/Conference")
    data = urllib.request.urlopen(req).read()

    print(data)

    f = open("./response.txt", "w")  # f = open("./response_iphone.html", "wb")
    f.write(str(data))
    f.close()
