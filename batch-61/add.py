#!/usr/bin/python
# https://docs.python.org/3/library/argparse.html

import sys

#print sys.argv

if len(sys.argv) != 3:
	print "syntax:{} <arg1>  <arg2>".format(sys.argv[0])
else:
	result = int(sys.argv[1]) + int(sys.argv[2])
	print "{}".format(result)