def celcius_fahrenheit(intemp):
 gradurf = intemp[:]
 for i in range(len(intemp)):
  gradurf[i] = intemp[i]*(9.0/5) + 32
	
 return gradurf


#print celcius_fahrenheit([0,10,20,30,40,50,60,70,80,90,100])