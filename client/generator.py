#!/usr/bin/env python3

### Password/Username/Port Generation
import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+', '?', '^','-','_','+','=']
# more = ['!','#','@','$','&','*','(',')','<','>','.','%']
### Password gen
def passwd_gen(num):
	passwd = []
	charlist = letters+numbers+symbols
	for i in range(num):
		randomchar = random.choice(charlist)
		passwd.append(randomchar)
	pwd = "".join(passwd)
	return pwd

### User generator ###

def username_gen():
	u = []
	charlist = letters
	for i in range(10):
		randomchar = random.choice(charlist)
		u.append(randomchar)
	usrname = "".join(u)
	return usrname

### Random port generator ###

def port_gen():
	p = []
	firstchar = random.choice("12345")
	p.append(firstchar)
	for i in range(4):
		randomchar = random.choice(numbers)
		p.append(randomchar)
	randport = "".join(p)
	return randport
