### System Checks
import parse
import generator
from subprocess import run, check_output
import lanip

def input():
	if parse.rpc_user == None:
		a = generator.username_gen().lower()
	else:
		a = args.rpc_user.lower()
	rpc_username = a

	if args.rpc_pass == None:
		b = generator.passwd_gen(60)
	else:
		b = args.rpc_pass
	rpc_passwd = b

	if args.keep_ssh_port == True:
		c = 22
	elif args.port == None:
		c = generator.port_gen()
	else:
		c = args.port
	port = c

	if args.username == 'firo':
		d = 'firo'
	else:
		d = args.username.lower()
	uname = d

	if args.password == None:
		e = generator.passwd_gen(15)
	else:
		e = args.password
	password = e

	if args.znodekey == None:
		g = "Missing ZnodePrivKey. Check Step 3 of Firo Masternode Guide"
	else:
		g = args.znodekey
	znodeprivkey = g

	if args.externalip == None:
		h = run(['curl', 'ifconfig.me'], capture_output=True)
		h = str(h.stdout).replace("b'", "").replace("'", "").strip()
	else:
		h = args.externalip
	externalip = h

	if args.output == 'output.txt':
		i = 'output.txt'
	else:
		i = args.output
	output = i

	if args.lan_address == None:
		j = ""
	else:
		j = args.lan_address
	lan_addr = j

	if args.subnet == None:
		k = ""
	else:
		k = args.subnet
	subnet = k

	current_dir = str(check_output('pwd')).replace("b'","").replace("\\n'","").strip()

	pub_key_file = args.key

	network_if = lanip.lanip.network_if

	broadcast = lanip.lanip.broadcast

	gateway = lanip.lanip.gateway

	network = lanip.lanip.network

	netmask = lanip.lanip.netmask
	print(netmask)
	return netmask, network, gateway, broadcast, network_if, pub_key_file, current_dir, subnet, lan_addr, output, externalip, znodeprivkey, password, rpc_passwd, rpc_username, port, uname
input()
