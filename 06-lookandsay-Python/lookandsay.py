# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	l=[]
	if(a==[]):
		return a
	else:
		count=1
		for i in range(1,len(a)):
			if(a[i-1]==a[i]):
				count+=1
			else:
				l.append((count,a[i-1]))
				count=1
		l.append((count,a[i]))
		return l
# print(lookandsay([3,3,8,-10,-10,-10]))
