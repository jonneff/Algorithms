"""
The challenge is to create a text content analyzer. This is a tool used by writers to find statistics such as 
word and sentence count on essays or articles they are writing.
Write a Python program that analyzes input from a file and compiles statistics on it. The program should output:

1. The total word count
2. The count of unique words 3. The number of sentences

Example output:
Total word count: 468 Unique words: 223 Sentences: 38

Brownie points will be awarded for the following extras:
1. The ability to calculate the average sentence length in words
2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times) 3. A list of words used, 
in order of descending frequency
￼
4. The ability to accept input from STDIN, or from a file specified on the command line.
"""
import sys
import operator

def analyzefile(filename):
  
  # open file read only, no unicode
  f=open(filename,'r')
  
  # read contents of file into a single string
  fstr=f.read()
  
  # make all words in string lower case, for getting # unique words later
  fstrlc=fstr.lower()
  
  # remove punctuation
  fstrnp = fstrlc.translate(string.maketrans("",""), string.punctuation)
  
  # split string on whitespace, put results into a list
  flist=fstrnp.split()
  """
  i have a list whose elements are all of the words in the file including
  duplicate words.
  
  length of flist is the total number of words in the file.
  """
  
  """
  now i need to iterate through the list.  
  if i sort first then i only have to check if a 
  new word is the same as the previous word.  if it is then i increment the
  count.  if it isn't the same then i create a new key-value pair for the dict.
  if i don't sort first then i have to compare against every key in the existing
  dict each time i read a new word.
  """
  # lists, unlike strings, are not immutable so i will sort the list in place
  flist.sort()
  
  # now iterate through and count unique words, where all duplicates are sorted
  # to be in sequence
  # create dict
  fdict={}
  
  # set previous_word to empty string
  previous_word=''
  
  # iterate through sorted list
  for word in flist:
    # is this the same as the previous word?  if so, increment count for word
    if word==previous_word:
      fdict[previous_word]+=1
    else:
    # set word, count key-value pair in hash table and update previous_word
      fdict[word]=1
      previous_word=word
  # length of fdict is number of unique words in file.  
  
  # add number of periods, question marks, and exclamation marks to get 
  # number of sentences
  numsentences = fstr.count('.') + fstr.count('?') + fstr.count('!')
  
  # i THINK this will provide a list of words in order of decreasing frequency
  sorted_words = sorted(fdict.items(), key=operator.itemgetter(1))
  
  f.close()
  return (len(flist), len(fdict), numsentences, sorted_words)
  

###

def main():
  filename = sys.argv[1]
  numwords, numuniquewords, numsentences, sorted_words = analyzefile(filename)
  print 'Total word count:  ' + numwords
  print 'Unique words:  ' + numuniquewords
  print 'Sentences:  ' + numsentences
  print 'Words sorted in decreasing frequency:  ' + sorted_words

if __name__ == '__main__':
  main()
