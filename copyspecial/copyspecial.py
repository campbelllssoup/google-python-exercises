#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""


def get_special_paths(dir):
    all_files = os.listdir(dir)
    file_names = []
    absolute_paths = []
 
    for filename in all_files:
        if re.search('__\w+__',filename):
            file_names.append(filename)

    for file in file_names:
        path = os.path.join(dir,file)    
        absolute_paths.append(os.path.abspath(path))
    
    return absolute_paths



def copy_to(paths,dir):
    print "Copying Files.."
    for path in paths:
        shutil.copy(path,dir)
    print "Copying complete."
    



def zip_to(paths,zippath):
    cmd = 'zip -j ' + zippath + ' ' + ' '.join(paths)
    print "Zipping files.."
    (status, output) = commands.getstatusoutput(cmd)
    



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir copy_dir files ...][--tozip zipfile files ...] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    copy_to(args,todir)
    sys.exit(0)


  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zip_to(args,tozip)
    sys.exit(0)

  for dir in args:
      for abs_path in get_special_paths(dir):
          print abs_path

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)


if __name__ == "__main__":
  main()
