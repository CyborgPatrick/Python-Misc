def maxdiff(values):
 maxdiff = 0
 for i in range(len(values)-1):
  absdiff = abs(values[i]-values[i+1])
  if absdiff > maxdiff:
   maxdiff = absdiff
 
 return maxdiff
 
 
 
#print maxdiff([23,5,1,0])