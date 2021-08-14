# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n=str(n)
	dict1={}
	for i in n:
		if(i not in dict1):
			dict1[i]=1
		else:
			dict1[i]+=1
	maximum=0
	val=''
	# print(dict1)
	for i in dict1:
		if(maximum<dict1[i]):
			maximum=dict1[i]
			val=i
		elif(maximum==dict1[i]):
			if(int(val)>int(i)):
				val=i 
			
		else:
			continue
	return int(val)
# print(mostfrequentdigit(int(input())))

			