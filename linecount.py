def linecount(filename):
 file = open(filename)
 counter = 0
 while 1:
  line = file.readline()
  if not line:
   break
  counter = counter + 1

 
 return counter

print linecount("linur.txt") 
