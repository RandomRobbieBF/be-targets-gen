#!/usr/bin/env python3
#
# Targets Generator to parse binaryedge.io json blob
#
# python3 be.py -f b3cef281-4s1a-4k45-8lv6-d42196c63b5f
#
# Author: RandomRobbieBF
import json
import argparse
import sys



parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", required=True, help="Binary Edge Json File")
args = parser.parse_args()
fname = args.file

try:
	with open(fname) as f:
		for line in f:
			json_string = json.loads(line)
			IP = json_string["target"]["ip"]
			PORT = str(json_string["target"]["port"])
			URL = ""+IP+":"+PORT+""
			print (URL)
			text_file = open(""+fname+".txt", "a")
			text_file.write(""+URL+"\n")
			text_file.close()
		
except KeyboardInterrupt:
		print ("Ctrl-c pressed ...")
		sys.exit(1)
				
except Exception as e:
		print('Error: %s' % e)
		sys.exit(1)
