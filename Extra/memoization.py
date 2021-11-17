cache = {}
def solve(n, coins, curr_coin_index):
	if n == 0:
		return 1
	if n < 0:
		return 0
	if (n, curr_coin_index) in cache:
		return cache.get((n, curr_coin_index))
	total = 0
	for i in range(0, curr_coin_index):
		total += solve(n - coins[i], coins, i)
	cache[(n, curr_coin_index)] = total
	return total

if __name__ == '__main__':
	print(solve(15, {1,5}, 0))