
def fibonacci_n():
 n = int(raw_input("Number of iterations: "))
 listi = []
 listi.append(0)
 listi.append(1)

 for i in range(1,n):
  listi.append(listi[i]+listi[i-1])	

 

 for i in range (len(listi)):
 	print listi[i]
 return listi

fibonacci_n()