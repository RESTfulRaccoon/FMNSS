import argparse
import local_fun as local_fun
#from subprocess import run


## Client OS Check For Commands

### ARG PARSE ###
parser = argparse.ArgumentParser(
	prog='send_nodes',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	usage='%(prog)s "107.191.53.17" "not_password1" "password2"',
	description='''
		todo
		todo
		todo
		''',
	add_help=True,
	allow_abbrev=False,
)

parser.add_argument('--pubkey', metavar='"'+local_fun.keypath+'"', help='Public key you would like to use for Secure Shell connections.')
parser.add_argument('server_ip', help='External IP address of server where node will be hosted.')
parser.add_argument('--superuser', metavar='raccoon', default='root', help='Name of Privlaged server user (default: %(default)s).')
parser.add_argument('supass', help='Password of root or firo superuser')
parser.add_argument('--usr', metavar='firo', default='firo', help='Name of Unprivlaged Firo Daemon user (default: %(default)s).')
parser.add_argument('--passwd', metavar='password1', help='Password of Firo Daemon user.')
parser.add_argument('--location',metavar=local_fun.discribe, default=local_fun.dflt, help='location of firod and firo-cli binary on client computer')
parser.add_argument('--rpc_user', help='Enter username for firo rpc. (default: will be 10 randomly generated letters.)')
parser.add_argument('--rpc_pass',help='Enter password for firo rpc. (default: will be randomly generated.)')
parser.add_argument('-p','--port', help='Define the port you would like ssh to use')
parser.add_argument('--sshkeypass', help='create a password for your ssh key, this is recommended but not required' )
parser.add_argument('wallet_password', help='''
			Your wallets encryption password.
			This is needed to generate your BLSPrivKey and register your node.
			It is required to have your wallet encrypted to run this script!!!.
					''')
parser.add_argument('--no_firewall', action='store_true', help='Dont allow this script to configure your server firewall (default: %(default)s).')
parser.add_argument('--keep_port', action='store_true', help='Use this if you would like to keep your ssh port as 22 (default: %(default)s)')
parser.add_argument('--nofinish', action='store_false', help='finsih the "wallet" setup manually after sync (default: %(default)s)')
parser.add_argument('-v','--verbose', action='store_true', help='Make script more verbose')
args = parser.parse_args()

### REQUIRED
ext = args.server_ip
supass = args.supass
walletpass = args.wallet_password

### AUTOGEN/VALIDATE INPUT
if args.verbose==True:
	def verbose(text):
		print(text)
else:
	def verbose(text):
		text
if args.rpc_user == None:
    a = local_fun.username_gen(10).lower()
else:
	a = args.rpc_user.lower()
local_fun.usr(a)
rpc_usrname = a

if args.rpc_pass == None:
	b = local_fun.rpc_passwd_gen(60)
else:
	b = args.rpc_pass
local_fun.rpc_pass(b)
rpc_passwd = b

if args.keep_port == True:
	c = 22
elif args.port == None:
	c = local_fun.port_gen()
else:
	c = args.port
local_fun.port(c)
port = c

if args.usr == 'firo':
	d = 'firo'
else:
	d = args.usr.lower()
local_fun.usr(d)
usr = d

if args.passwd == None:
	e = local_fun.usr_passwd_gen(15)
else:
	e = args.passwd
passwd = e


if args.pubkey == None:
	i = print("todo!: checkinfo.pubkey")
else:
	i = args.pubkey		
pubkey = i

if args.superuser == None:
	j = "root"
else:
	j = args.superuser
suusr = j


if args.sshkeypass == None:
	k = ""
else:
	k = args.sshkeypass
sshkeypass = k

nofinish = args.nofinish