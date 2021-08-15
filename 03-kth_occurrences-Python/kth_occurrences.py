# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.

import operator

def fun_kth_occurrences(s, n):
	maximum=0
	dict1={}
	for i in s:
		if i not in dict1:
			dict1[i]=1
		else:
			dict1[i]+=1
	# print(dict1)
	a=sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)
	return a[n-1][0]
	



