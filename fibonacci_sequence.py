def dynamic_fib(n):
	store_fib = [] #Store the previous fib values
	
	#Store the base cases f(0) = 0 and f(1) = 1
	store_fib.append(0) 
	store_fib.append(1)
	
	if n == 0:
		return store_fib[0]
		
	if n == 1:
		return store_fib[1]
	
	#Compute the remaining fib values
	for i in range(1, n):
		store_fib.append(store_fib[i] + store_fib[i-1])
			
	return store_fib[n]
