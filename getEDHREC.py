#!/usr/bin/env python3
import sys,re
"""
This script will take the raw website data from EDHREC and output a list off all cards on the commander page in a list, seperated by newlines
"""

def main(argv):
    
    output_list = []
    with open("_RAW.txt", 'r') as in_file:
        
        REGEX = r'"Card_name__Mpa7S">([\D ]+)</span>'
        for line in in_file:
            
            found_list = re.findall(REGEX,line)
            
            #if nothing is found, there no use continueing.
            if len(found_list) == 0: continue
            #print(found_list)
            for found_item in found_list:
                output_list.append("1x " + found_item + "\n")
                
                
    with open("output.txt", 'w') as out_file:
        for item in output_list:
            out_file.write(item)
if __name__ == "__main__":
    main(sys.argv)
