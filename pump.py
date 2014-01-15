def pump(instring):
 str = ''
 for i in range(len(instring)):
  if instring[i] in ('0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9'):
   num = int(instring[i])
   try:
    for n in range(num):
     str = str+instring[i+1]
   except:
    pass
  else:
    str = str+instring[i]
 
 return str

print pump('123456789')