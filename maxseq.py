def maxseq(instring):
 temp = instring[0]
 counter = 1
 maxcount = 1
 
 for i in range(1,len(instring)):
  if instring[i] == temp:
   counter = counter +1
  elif instring[i] != temp:
   if counter > maxcount:
    maxcount = counter
   temp = instring[i]
   counter = 1
   
 if counter > maxcount:
  maxcount = counter
    
   
 return maxcount
 
#print maxseq('aabcfffjkiiiiiiiklloodbshersdkggssiiiiiiii')
