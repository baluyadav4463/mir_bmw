#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Dec  3 27:40:20 2018

python3 Learning_studio_dataset directory_to_your_csv name_of_images_folder 

output will be saved in a new csv file  into same terminal directory
@author: Mirlab
"""


import csv
import sys

def main():
    try:
        if (len(sys.argv) != 3):
            print('Give a csv file location and the images file name')
            return
        reading_file(sys.argv[1],sys.argv[2])        
    except KeyboardInterrupt:
        print ('\nShutdown requested. Exiting...')




def reading_file(self,name):
    f = open(self)
    csv_file = csv.reader(f)
    lines=list(csv_file)
    with open('train.csv', mode='w',newline='') as csv_files:
            fieldnames = ['Images', 'ratings']
            writer = csv.DictWriter(csv_files, fieldnames=fieldnames)
            writer.writeheader()
            for i in range (len(lines)):
                print(lines[i][0])
                first= "./"+name+"/"+lines[i][0]+".jpg"
                second=lines[i][1]
                writer.writerow({'Images':first,'ratings':second})

            
 
if __name__ == '__main__':
    main()
