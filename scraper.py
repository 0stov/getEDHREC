#!/usr/bin/env python3
import sys
import urllib.request, urllib.parse, urllib.error
import re

def main(argv):
    url = input("Enter website to be scraped: \t")
    # url = 'https://en.wikipedia.org/wiki/List_of_Roman_legions'

    #strips everything from the url except the last string before the '/'
    #used for test file nameing
    #ie. 'https://en.wikipedia.org/wiki/List_of_Roman_legions' becomes 'List_of_Roman_legions_RAW'
    name = str(re.findall('/[\w]+$', url)).replace('/', '').replace("'", '').replace('[','').replace(']', '') + "_RAW"



    fhand = urllib.request.urlopen(url)


    with open("{}.txt".format(name), "w", encoding="utf-8") as f:
        for line in fhand:
            f.write(line.decode().strip() + '\n')

    

if __name__ == "__main__":
    main(sys.argv)
