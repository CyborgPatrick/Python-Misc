def wordcount(filename):
 totcount = 0
 worddict = { };
 file = open(filename)
 
 for line in file:
  for word in line.split():
   totcount += 1   
   if worddict.has_key(word):
    worddict[word] = worddict[word] + 1;
   else:
    worddict[word] = 1;
 
 
 w = list(worddict.keys())
 
 return (len(w), totcount)

#print wordcount('wordctest.txt')