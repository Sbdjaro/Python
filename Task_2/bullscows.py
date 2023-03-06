def bullscows(guess: str, secret: str) -> (int, int):
	first = 0
	for i in range(min(len(guess),len(secret))):
		if guess[i]==secret[i]:
			first+=1
	g=set(list(guess))
	s=set(list(secret))
	second = len(set.intersection(g, s))
	return first,second
	
print(bullscows("ропот", "полип"))
