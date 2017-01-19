# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 12:10:32 2017

@author: stpl
"""
import sys

def main():
      if len(sys.argv) != 3:
          sys.stderr.write("No more than three arguments : " + sys.argv[0] + " " + str(sys.argv[1:(len(sys.argv))]));
          sys.stderr.flush();
          exit(2);
    
      else:
          filename = sys.argv[1];
          needle = sys.argv[2];
          
      counter = 0;
      file_handle = open(filename);
      for line in file_handle.readline():
          words = line.split(" ");
          
          for word in words:
              if word == words[-1]:
                  word = word[:-1];
                 
              if word == needle:
                  counter += 1;
            
      print(counter);
      
if __name__ == "__main__":
    main();
      