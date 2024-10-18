### Password/Username/Port Generation
import random
import distro

letters = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['+','-','_','=']
more = ['!','#','@','$','&','*','(',')','<','>','.','%','?','^']

### Distro Information
dist = distro.id()

if dist == 'ubuntu' or 'debian':
	discribe='common linux Download path'
	dflt='/usr/local/bin/'
	check_path=['/home/$USER/Downloads/firo']
	keypath='/home/$USER/.ssh/'
	
	#anyother disto specific commands or paths
elif dist == 'macOS':
	discribe="common macOS path"
	dflt='where ever it should run from'
	check_path="where it could be if its not where it should be"
	keypath='/home/$USER/.ssh/'
	#anyother disto specific commands or paths
elif dist == "Windows":
	discribe="windows sucks"
	dflt="del system32"
	check_path="where it could be if its not where it should be"
	keypath='/home/$USER/.ssh/'
	#anyother disto specific commands or paths


### Daemon User Password Gen
def usr_passwd_gen(num):
	passwd = []
	charlist = letters+numbers+symbols+more
	for i in range(num):
		randomchar = random.choice(charlist)
		passwd.append(randomchar)
	usrpwd = "".join(passwd)
	return usrpwd

### RPC Username & Password generator ###
def username_gen(num):
	u = []
	charlist = letters
	for i in range(num):
		randomchar = random.choice(charlist)
		u.append(randomchar)
	rpcname = "".join(u)
	return rpcname

def rpc_passwd_gen(num):
	passwd = []
	charlist = letters+numbers+symbols+more
	for i in range(num):
		randomchar = random.choice(charlist)
		passwd.append(randomchar)
	rpcpwd = "".join(passwd)
	return rpcpwd

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

## sanatize

def rpc_pass(v):
    print("v_rpc_pass: "+v)
    #check that the password doesnt use "#", might want to make it more strict

def ext(v):
     print("v_ext: "+v)
    #check that its not an internal ip && ip is valid

def subnet(v):
     print("v_subnet: "+v)
    #check against netmasks and subnets "255.255.255.0 or 24" should both work
    #change the netmask to a subnet on the fly here if needed.

def port(v):
    print("v_port: "+v)
    #check against commonly used ports, inform user port should be above 10000

def usr(v):
	print("v_usr: "+v)
    #alpha only exit()  if fails

#generate ssh-key
def sshkeygen():
	print("todo!: local_fun.sshkeygen")
#copy ssh-key to server
def sshcopykey():
	print("todo: local_fun.sshcopykey")