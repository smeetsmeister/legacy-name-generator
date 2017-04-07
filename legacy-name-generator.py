#!/usr/bin/python

import sys, getopt, random

def getRandomWords(length):
   words = ['v1', 'v2', 'v3', 'final', 'draft', 'tested', 'updated', 'review', 'final2', 'new', 'todo', 'with-comments', 'incomplete'];

   return random.sample(words, length);


def getLegacyName(filename, seperator, length):
   #Split actual name and extension
   name, extension = filename.split(".");

   #get random words for length
   randomWords = getRandomWords(length);

   #set original file name as starting point
   legacyName = name;

   #set seperators
   for val in randomWords:
    legacyName+= seperator + val;

   #add original extension
   legacyName+= "." + extension;

   return legacyName;

def main(argv):
   filename = ''
   seperator = '_'
   length = 4

   try:
      opts, args = getopt.getopt(argv,"hf:s:l:",["file=","seperator=", "length="])
   except getopt.GetoptError:
      print 'test.py -f <filename> -s <seperator>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'legacy-name-generator.py -f <filename> -s <seperator> -l <length>'
         sys.exit()
      elif opt in ("-f", "--file"):
         filename = arg
      elif opt in ("-s", "--seperator"):
         seperator = arg
      elif opt in ("-l", "--length"):
         length = int(arg)

   if filename != '':
      legacyName = getLegacyName(filename, seperator, length);
      print 'New Legacy name is: ', legacyName
   else:
      print 'No legacy filename was entered.'

if __name__ == "__main__":
   main(sys.argv[1:])