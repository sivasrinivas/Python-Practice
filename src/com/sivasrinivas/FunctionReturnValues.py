'''
Created on Dec 16, 2013

@author: Siva
'''
def add(a, b):
    print "adding %r + %r" % (a, b)
    return a+b

def divide(a, b):
    print "dividing %r / %r" % (a, b)
    return a/b, a%b


print add(2,3)

divident, remainder = divide(4,2)

print "divident : %r, remainder : %r" % (divident, remainder)
    