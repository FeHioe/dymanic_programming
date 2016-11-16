def coin_change(change, coin_list):
	store_coins = []
	store_coins.append(0)
	
	for i in range(1, change+1):
		store_coins.append(-99)
		for coin in coin_list:
			if (i - coin >= 0) and (store_coins[i - coin] != -99) and (store_coins[i] > store_coins[i - coin] or store_coins[i] == -99):
				store_coins[i] = 1 + store_coins[i - coin]
				
	if store_coins[change] == -99:
		return "Not possible."
	else:
		return "Can be made out of " + str(store_coins[change]) + " coins."
