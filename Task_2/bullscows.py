import random
import urllib.request as ur
import argparse

def bullscows(guess: str, secret: str) -> (int, int):
	first = 0
	for i in range(min(len(guess),len(secret))):
		if guess[i]==secret[i]:
			first+=1
	g=set(list(guess))
	s=set(list(secret))
	second = len(set.intersection(g, s))
	return first,second
	
def inform(format_string: str, bulls: int, cows: int) -> None:
	print(format_string.format(bulls,cows))
	
def ask(prompt: str, valid: list[str] = None) -> str:
	print(prompt)
	s = input()
	while s not in valid:
		print("Invalid word")
		print(prompt)
		s = input()
	return s
	
def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
	secret = random.choice(words)
	print(secret)
	attempts = 0
	while True:
		answer = ask("Введите слово: ", words)
		attempts+=1
		res = bullscows(answer,secret)
		inform("Быки: {}, Коровы: {}",*res)
		if res[0]==len(secret):
			print("You win!")
			print(f"You used {attempts} attempts")
			break	
		
def prepare_words(URL: str, lenght: int) -> list[str]:
	l = []
	data = ur.urlopen(URL) # it's a file like object and works just like a file
	for line in data: # files are iterable
		w = line.decode()[0:-1]
		if len(w)==lenght:
			l.append(w)
	return l
	
parser = argparse.ArgumentParser()
parser.add_argument('dictionary', type=str, help="URL to dictionary")
parser.add_argument('lenght', type=int, help="Select word's lenght")
args = parser.parse_args()

words = prepare_words(args.dictionary,args.lenght)
gameplay(ask,inform,words)
