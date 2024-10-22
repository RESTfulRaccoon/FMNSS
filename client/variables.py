from sendnodes import args
import local_fun as local_fun
import distro
from pathlib import Path

### CLIENT DISTRO SPICIFIC INFORMATION

dist = distro.id()
home = str(Path.home())

if dist == 'ubuntu' or 'debian':
	#where it should be
	dflt='/usr/local/bin/'
	#where it could be
	#check_path=[home+'Downloads/firo', home+'Desktop/firo']
	keypath=home+'/.ssh/'
	#anyother disto specific commands or paths
elif dist == 'macos':
	#where it should be
	dflt='where ever it should run from'
	#where it could be
	#check_path="where it could be if its not where it should be"
	keypath=home+'/.ssh/'
	#anyother disto specific commands or paths

elif dist == "windows":
	#where it should be
	dflt="del system32"
	#where it could be
	#check_path="where it could be if its not where it should be"
	keypath=home+'/.ssh/'



### REQUIRED
ext = args.server_ip
supass = args.superuser_pass
walletpass = args.wallet_password

### VERBOSE

if args.verbose==True:
	def verbose(text):
		print(text)
else:
	def verbose(text):
		text

### RPC USERNAME

if args.rpc_user == None:
    a = local_fun.username_gen(10).lower()
else:
	a = args.rpc_user.lower()
local_fun.usr(a)
rpc_usrname = a

### RPC PASSWORD

if args.rpc_pass == None:
	b = local_fun.rpc_passwd_gen(60)
else:
	b = args.rpc_pass
local_fun.rpc_pass(b)
rpc_passwd = b

### SSH PORT
if args.port != None and args.keep_port == True:
	c = args.port
elif args.keep_port == True:
	c = 22
elif args.port == None:
	c = local_fun.port_gen()
else:
	c = args.port
local_fun.port(c)
port = c

### UNPRIVLAGED USERNAME

if args.usr == 'firo':
	d = 'firo'
else:
	d = args.usr.lower()
local_fun.usr(d)
usr = d

### UNPRIVLAGED USERPASSWORD
if args.passwd == None:
	e = local_fun.usr_passwd_gen(15)
else:
	e = args.passwd
passwd = e

### SSH KEY LOCATION
keyname = args.ssh_key_name

### SUPER USER NAME
suusr = args.superuser

### (OPTIONAL) SSH KEY PASSWORD
sshkeypass = args.sshkeypass

### CLIENT WILL FINISH SET UP ONCE SERVER IS SYNCED
nofinish = args.nofinish

clean_up = ['rm','-rf','./__pycache__']