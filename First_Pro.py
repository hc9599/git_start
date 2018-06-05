import sys
import os
import csv
import fileinput
import numpy as np

'''
user_input = str(input("Emter the text you want to search: "))
#tempfile.readline().strip()
#with open("C:\\Users\\Himanshu Choudhary\\Downloads\\WhatsAppChat.txt","r+", encoding="utf8")
n = 0
with open("C:\\Users\\Himanshu Choudhary\\Downloads\\WhatsAppChat.txt","r+", encoding="utf8") as searchfile:
    for line in searchfile:
        if user_input == line:
            print("found")
        else:
            break
'''

def search_text():

    file  = open('C:\\Users\\Himanshu Choudhary\\Downloads\\WhatsAppChat.txt', 'r', encoding="utf8").read()
    search_string  = input("Enter text used by Asha: ")
    count = file.count(search_string)
    print(count)

b = int(input("Enter how many input you want to try: "))
i=1
for i in range(b):
    search_text()


