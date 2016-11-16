#For example, length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

def LIS(lst):
	store = [1] * len(lst)
	
	for i in range (1 , len(lst)):
		for j in range(0 , i):
			if lst[i] > lst[j] and store[i]< store[j] + 1 :
				store[i] = store[j]+1
	return store
