'''
Created on Dec 16, 2013

@author: Siva
'''

#two arguments function with unpacking
def func_two(*argv):
    arg1, arg2 = argv
    print "argument 1: %r, argument 2: %r" % (arg1, arg2)

#two arguments function
def func_two_again(arg1, arg2):
    print "argument 1: %r, argument 2: %r" % (arg1, arg2)
    
func_two("siva", "srinivas")
func_two_again("siva", "srinivas")