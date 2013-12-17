'''
Created on Dec 16, 2013

@author: Siva
'''
from sys import argv

print "Reading file:","sample.txt"
target = open("sample.txt")
print target.read()
target = open("sample.txt", 'w')
print "Clearing file content..."
target.truncate()
line1 = raw_input("Enter line1: ")
target.write(line1)
target.close()

print "Reading file again..."
target = open("sample.txt")
print target.read()