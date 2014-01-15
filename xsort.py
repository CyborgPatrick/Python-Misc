def xsort(words):
 listi = words[:]
 listi.sort()
 place = 0
 xstr = []
 fs = 0
 start = 0
 
 for i in range(len(words)):
  str = listi[i]
   
  
  if str[0] == 'x':
   if fs == 0:
    start = i
    fs = 1
   xstr.insert(place,str)
   place = place + 1
  
 xstr.sort()
 result = xstr + listi[:start] + listi[start+place:]
  

 return result
 
print xsort(['epli','ananas','anas','xenon','xorfar','ups','yes','burgeer','raven','coke','xylofone','bord','stoll'])
