#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# COMPLETED!!!

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""
implement the extract_names(filename) function which takes 
the filename of a baby1990.html file and returns the data 
from the file as a single list -- the year string at the
start of the list followed by the name-rank strings in 
alphabetical order. ['2006', 'Aaliyah 91', 'Abagail 895',
'Aaron 57', ...]. Modify main() so it calls your 
extract_names() function and prints what it returns 
(main already has the code for the command line argument parsing)
"""



"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]

  When finishing this function return the baby names strings instead of 
  printing so that it will write to the summary.txt file
  """
  solution = []
  all_names = []

  f = open(filename, 'r')
    
  all_text = f.read()
  body_text_list = re.findall(r'<body.*>[\w\b\W]*',all_text)
  body_text = ''.join(body_text_list)

  year_info_list = re.findall(r'Popularity in \d+', body_text)
  year_info = ''.join(year_info_list)
  year = re.search(r'\d+', year_info).group()
  solution.append(year)
  
  baby_info_list = re.findall(r'<tr align="right"><td>(.*)</td><td>(.*)</td><td>(.*)</td>',body_text)
  
  for rank in baby_info_list:
      boy_name = '%s %s' % (rank[1], rank[0])
      girl_name = '%s %s' % (rank[2], rank[0])
      all_names.extend([boy_name, girl_name])      

  all_names = sorted(all_names)
  solution.extend(all_names)

  f.close()
 
  return solution

  


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
      print 'usage: [--summaryfile] file [file ...]'
      sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
      summary = True
      del args[0]
    


  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary == True:
      f = open('summary.txt', "w")
      print "Writing to summary.txt"
      print "..."
      for file in args:
              
          for match in extract_names(file):
              f.write('%s\n' % match)

      f.close()

  else:
      for file in args:
          for match in extract_names(file):
             print match

  
if __name__ == '__main__':
  main()
