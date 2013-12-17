'''
Created on Dec 16, 2013

@author: Siva
'''
from os.path import exists

source = open("sample.txt")
content = source.read()
print "File content:\n", content
print "Does output file exists:", exists('temp.txt')
target = open("temp.txt",'w')
target.write(content)

source.close()
target.close()