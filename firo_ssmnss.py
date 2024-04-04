#!usr/bin/python3
import socket
import os
import sys
from pwd import getpwall
from subprocess import run, check_output
import argparse
import textwrap
import random
import requests
import tarfile
import shutil
import glob
import distro
import fcntl
import struct
import ipaddress


### DEPENDS: iptables, python3-requests, python3-distro

### Argument Parser ###
parser = argparse.ArgumentParser(
	prog='firo_ssmnss',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	usage='%(prog)s <server_public_ip_address> <server_username> <server_superuser_password>',
	description=textwrap.dedent('''
	Firo Server Side Masternode Start Script
	Automatic configuration of server for Firo Masternode.
	'''),
	add_help=True,
	allow_abbrev=False,
	)

parser.add_argument('-k', '--key', metavar='string format of public ssh key', help='Public key you would like to use for Secure Shell connections.')
parser.add_argument('-u', '--username', metavar='raccoon', default='firo', help='Name of Firo Daemon user (default: %(default)s).')
parser.add_argument('-p', '--password', metavar='CR@ZY_G00D_PA55W0RD', help='Password of super user, or root if no username provided.')
parser.add_argument('-o','--output', metavar='output.txt', default='output.txt',help='Name of output file to be saved (default: %(default)s).')
parser.add_argument('-l', '--lan_address', metavar='192.168.1.111', help='The LAN addess of your masternode (default: dhcp4 Server generated address.)')
parser.add_argument('-s', '--subnet', metavar='/24', help='subnetet of local network of masternode. (default: Acuired from server current ipv4 address.)')
parser.add_argument('-ru', '--rpc_user', metavar='<firo_rpc_username>', help='Enter username for firo rpc. (default: will be randomly generated.)')
parser.add_argument('-rp', '--rpc_pass', metavar='<firo_rpc_password>',help='Enter password for firo rpc. (default: will be randomly generated.)')
parser.add_argument('-P', '--port', metavar='31337', help='Define the port you would like ssh to use')
parser.add_argument('-z', '--znodekey', metavar='', help='Your znodeblsprivkey')
parser.add_argument('-e', '--externalip', help='The external IP if your Masternode, (default: will be taken from system command `ifconfig.me`)')
parser.add_argument('--no_firewall', action='store_true', help='Dont allow this script to configure your server firewall (default: %(default)s).')
parser.add_argument('--keep_ssh_port', action='store_true', help='Use this if you would like to keep your ssh port as 22 (default: %(default)s)')
parser.add_argument('--keep_sshd_config', action='store_true', help='Use this if you would like to keep your sshd_config file as it is (default: %(default)s).')
args= parser.parse_args()

### ARG PARCE VALIDATION ###
# Make sure user doesnt use something funky
def validator():
	print("todo!")

### Checks ###
if sys.version_info[0] == 3 and sys.version_info[1] >= 6:
	pass
else:
	print("Please update your python version to at least Python3.6")
	exit()

try:
	dist = distro.id()
	dist_ver = distro.version()
except OSError as error:
	print(error)
	exit()

if dist == 'ubuntu' or 'debian':
	manager = 'apt'
else:
	print("Package manager not currently supported!!!\nExiting...")
	exit()

### Password generator ###
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '%', '&', '*', '+', '?', '^']
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
		randomchar = random.choice("1234567890")
		p.append(randomchar)
	randport = "".join(p)
	return randport

### Variables ###

arch = str(check_output('arch')).replace("b'","").replace("\\n'","").strip()
try:
	firo_core_version = requests.get('https://api.github.com/repos/firoorg/firo/releases/latest')
except OSError as e:
	print(e)
	exit()
numb = 0
if arch == 'x86_64':
	numb = 1
else:
	print("This script is designed for Linux based systems on ARM or x86_64 architecture\nExiting...")
	exit()
tarball = "".join(firo_core_version.json()["assets"][numb]["browser_download_url"].split("/")[-1])

current_dir = str(check_output('pwd')).replace("b'","").replace("\\n'","").strip()

pub_key_file = args.key

network_interface = ""

broadcast = ""

gateway = ""

network = ""

netmask = ""

wifi_pass = ""

### Arg variables ###
if args.rpc_user == None:
	a = username_gen().lower()
else:
	a = args.rpc_user.lower()
rpc_username = a
if args.rpc_pass == None:
	b = passwd_gen(60)
else:
	b = args.rpc_pass
rpc_passwd = b
if args.keep_ssh_port == True:
	c = 22
elif args.port == None:
	c = port_gen()
else:
	c = args.port
port = c
if args.username == 'firo':
	d = 'firo'
else:
	d = args.username.lower()
uname = d
if args.password == None:
	e = passwd_gen(15)
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

### Enusre admin privs ###
	
if os.geteuid() == 0:
	pass
else:
	print("You must be root to run this program!")
	print("Please use `sudo python3 firo-ssmnss.py` or run the command `su -` to become root user and try again")
	print("Exiting program...")
	exit()

o = open('/root/'+output, 'w')
o.write("This is your output file all of the information from this script will be gathered here\nSafe this information somewhere safe!!! Failure to do so might result in needing to completely remake your Masternode!!!\n\n\n")
o.close
o = open('/root/'+output, 'a')
### Local network ###

def get_local_ip():
	global lan_addr
	global subnet
	global broadcast
	global gateway
	global network_interface
	global network
	global netmask
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('1.1.1.1', 80))
	my_ip = s.getsockname()[0]
	s.close()
	iface = socket.if_nameindex()
	n = 0
	for n in range(len(iface)):
		i = iface[n][1]
		try: 
			subnetet_mask = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack(b'256s', i.encode()))[20:24])
		except OSError as error:
			print(error)
	my_network = ipaddress.IPv4Network(my_ip+'/'+subnetet_mask, strict=False)
	netmask = subnetet_mask
	network_interface = i

	if lan_addr == "":
		lan_addr = str(my_ip)

	if subnet == "":
		subnet = str(my_network).split("/")[1]
	
	network = str(my_network).split("/")[0]
	broadcast = lan_addr[:lan_addr.rfind('.')+1] + '255'
	gateway = lan_addr[:lan_addr.rfind('.')+1] + '1'

	o.write(
f'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx FIRO CONFIG xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

RPC Username: {rpc_username}
RPC Password: {rpc_passwd}
ZnodePrivKey: {znodeprivkey}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxx USER INFORMATION xxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Firo Daemon User: {uname}
Daemon User Password: {password}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxx NETWORK INFORMATION xxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Local IP Address: {lan_addr}/{subnet}
Local Network: {network}
Local Subnet: {netmask}
Gateway IP Address: {gateway}
Broadcast IP Address: {broadcast}
External IP Address: {externalip}
SSH Port: {port}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxx ERRORS xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
)
	o.close
### Create static ip address ###

def static_ip():
	print("========== Creating static ip address ==========\n")
	if dist == 'debian' or ('ubuntu' and dist_ver <= '16'):
		f = open('/etc/network/interfaces', 'w')
		if 'en' in network_interface:
			f.write('#Generated by Firo Masternode Startup Script\n\n#primary network interface\nauto '+network_interface+'\niface '+network_interface+' enp0s3 inet static\n\taddress '+lan_addr+'/'+subnet+'\n\tnetwork '+network+'\n\tbroadcast '+broadcast+'\n\tgateway '+gateway+'\n\tdns-nameserver 1.1.1.1\n\tdns-nameserver 1.0.0.1\n\n#loopback interface\nauto lo\niface lo inet loopback')
		elif 'wl' in network_interface:
			print("This script currently doesn't work with wifi")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
		elif 'tun' or 'nord':
			print("Seems like you are connected to a VPN, please disconnect and try again")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
		else:
			print("Not able to gather required information!")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
		f.close
	
	elif dist == 'ubuntu' and dist_ver > '16': 
		f = open("/etc/netplan/01-netcfg.yaml", "w")
		if "en" in network_interface:
			f.write('#Created by Firo Masternode Startup Script\n\nnetwork:\n\tversion: 2\n\trenderer: NetworkManager\n\tethernets:\n\t\t'+network_interface+':\n\t\t\taddresses:\n\t\t\t\t- '+lan_addr+'\n\t\t\tnameservers:\n\t\t\t\taddresses: [1,1,1,1, 1.0.0.1]\n\t\t\troutes:\n\t\t\t\t- to: default\n\t\t\t\t  via:'+gateway)
		elif "wl" in network_interface:
			print("This script currently doesn't work with wifi")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
		elif 'tun' or 'nord':
			print("Seems like you are connected to a VPN, please disconnect and try again after disconnecting")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
		else:
			print("Not able to gather required information!")
			print("==========Failed to create a static ip address!==========\n")
			o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
			o.close
	else:
		print("Static IP configuration only avilable for Debian based servers.")
		print("==========Failed to create a static ip address!==========\n")
		o.write(
'''
FAILED TO CREATE STATIC IP ADDRESS!
'''
)
		o.close
### Sshd configuration ###

def sshd_conf():
	print("========== Configuring SSHD... ==========\n")
	f = open('/etc/ssh/sshd_config', 'a')
	f.write('PermitRootLogin no\nMaxAuthTries 3\nMaxSessions 3\n')
	if args.key == None:
		pass
	else:
		f.write('PasswordAuthentication no\n')
	if port == '22':
		pass
	else:
		f.write('Port '+port+'\n')
	f.close
	if os.path.exists("/etc/ssh/sshd_config.d/50-cloud-init.conf"):
		os.remove('/etc/ssh/sshd_config.d/50-cloud-init.conf')
	if os.path.exists("/etc/sysconfig/sshd-permitrootlogin"):
		os.remove("/etc/sysconfig/sshd-permitrootlogin")
	print("\t========== Complete ==========\n\n")

### Firewall configuration with UFW ###

def deb_firewall_config():
	if args.no_firewall == False:
		print("========== Configuring IPTables... ==========\n")
		# Flush any previous rules
		run(['iptables', '-F'])
		# Whitelist
		run(['iptables', '-P', 'INPUT', 'DROP'])
		run(['iptables', '-P', 'FORWARD', 'DROP'])
		run(['iptables', '-P', 'OUTPUT', 'DROP'])
		# Ensure loopback traffic is configured
		run(['iptables', '-A', 'INPUT', '-i', 'lo', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-o', 'lo', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-s', '127.0.0.1/8', '-j', 'DROP'])
		# Default Deny and Allow:
		run(['iptables', '-A', 'OUTPUT', '-p', 'tcp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-p', 'udp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-p', 'icmp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'udp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'icmp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		# Allow SSH and Masternode port
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-m', 'state', '--state', 'NEW', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '8168', '-m', 'state', '--state', 'NEW', '-j', 'ACCEPT'])
		run(['iptables', '-t', 'nat', '-A', 'OUTPUT','-s', network+'/'+subnet, '-d', externalip, '-j', 'DNAT', '--to-destination', lan_addr])
		# DROP all ip6 traffic
		run(['ip6tables', '-P', 'INPUT', 'DROP'])
		run(['ip6tables', '-P', 'OUTPUT', 'DROP'])
		run(['ip6tables', '-P', 'FORWARD', 'DROP'])
		run(['iptables-save'])
		print("\t========== Complete ==========\n\n")

### Add user if user doesn't exist ###
	
def adduser():
		print(f"========== Checking if {uname} exists as a user ==========\n")
		usernames = [x[0] for x in getpwall()]
		if uname in usernames:
			print(f"{uname} is already a user, skipping this step")
		else:
			
			print(f"========== Adding {uname} user... ==========\n")
			run(['useradd', '-m', uname])
			usr = 'firo:'+password
			cmd = 'printf "'+usr+'" | chpasswd'
			os.system(cmd)
			print("\t========== Complete ==========\n\n")

### Add ssh key if provided ###

def addkey():
	if args.key == None:
		pass
	else:
		print(f"========== Adding ssh key to {uname} home directory ==========\n")
		f = open('/home/'+uname+'/.ssh/authorized_keys', 'w')
		f.write(args.key)
		f.close
		print("\t========== Complete ==========\n\n")

### Download Firo tarball and CHECKSUMS###

def download_firod():
	charch = 0

	if arch == 'x86_64':
		charch = 1
	
	print("========== Downloading Firo Binaries tarball and Checksums... ==========\n")
	run(['wget', '-q', firo_core_version.json()['assets'][charch]['browser_download_url']])
	run(['wget', '-q', firo_core_version.json()['assets'][6]['browser_download_url']])
	print("\t========== Complete ==========\n\n")

### Validate intrgrity of tarball with CHECKSUMS ###

def checksum():
	vers = 'aarch64'

	if arch == 'x86_64':
		vers = 'linux64'

	print("========== Checking download integrity ==========\n")

	for lines in open('SHA256SUMS', 'r'):
		if vers in lines:
			line = lines
   
	check1 = str(check_output(['sha256sum', tarball])).replace("b'"," ").replace("\\n'","").strip()
	check2 = str(line).strip()
	if check1 == check2:
		print("========== \tIntegrity Verified... ==========\n")
	else:
		shutil.rmtree(current_dir+"/"+tarball)
		shutil.rmtree(current_dir+'/SHA256SUMS')
		o.write(
'''
Could not verify integrity of Firo-Tarball
'''
		)

### Extract tarball and move binaries to /usr/local/bin ###

def extract_and_move():
	print("========== Extracting Firo Binaries ==========\n")
	tar = tarfile.open(tarball.strip(), "r:gz")
	tar.extractall()
	tar.close
	print("\t========== Complete ==========\n\n")
	print('========== Moving binaries to /usr/local/bin ==========')
	for p in glob.glob(current_dir+'/firo-*/bin/firo*'):
		shutil.copy(p, "/usr/local/bin/")
		print("Moved "+p+" to /usr/loca/bin/")
	print("\t========== Complete ==========\n\n")
	shutil.copy('/root/'+output, '/home/'+uname+'/')

### Create Firod config file ###

def create_config():
	print("========== Writing firo.conf file ==========\n")
	try:
		os.mkdir('/home/'+uname+'/.firo')
	except OSError as error:
		print(error)
		pass
	f = open('/home/'+uname+'/.firo/firo.conf', 'w')
	f.write(f'#----\nrpcuser={rpc_username}\nrpcpassword={rpc_passwd}\nrpcallowip=127.0.0.1\n#----\nlisten=1\nserver=1\ndaemon=1\nlogtimestamps=1\ntxindex=1\n#----\nznode=1\nexternalip={externalip}:8168\nznodeblsprivkey={znodeprivkey}')
	f.close
	print("\t========== Complete ==========\n\n")

### Create Firod system daemon ###

def create_service():
	f = open("/etc/systemd/system/firod.service", "w")
	f.write(
f'''
[Unit]
Description=Firo daemon
After=network.target

[Service]
Type=forking
Restart=always
RestartSec=30

User={uname}
Group={uname}
PIDFile=/home/{uname}/.firo/firod.pid

ExecStart=/usr/local/bin/firod
ExecStop=/usr/local/bin/firo-cli stop

[Install]
WantedBy=multi-user.target
'''
	)
	f.close

### Create logrotate for Firod ###

def rotate_logs():
	f = open("/etc/logrotate.d/firo", "w")
	f.write("/home/"+uname+"/.firo/debug.log {\ndaily\nmissingok\nrotate 28\ncompress\ncopytruncate\n}")
	f.close

### Ensure enough memory and virtual memory, add if needed ###

def make_swap():
	print("Checking if swap exists...")
	swap = run(['free'], capture_output=True)
	swap = str(swap.stdout).replace("b'", "").replace("\\n", " ").replace("\\t", " ").replace("'", "").split()
	pswap = run(['cat','/proc/swaps'], capture_output=True)
	pswap = str(pswap.stdout).replace("b'", "").replace("\\n", " ").replace("\\t", " ").replace("'", "").split()
	mem = swap[7]
	mem = round(int(mem)*.931323/1000000)

	if "file" in pswap:
		dex=pswap.index('file')
		flocation = pswap[dex+1]
	else:
		flocation = None
    
	if "Swap:" in swap:
		dex = swap.index("Swap:")
		swap = swap[dex+1]
		swap = round(int(swap)*.931323/1000000)
	else:
		swap = None

	if mem >= 4 and swap != None:
		print("Sufficent memory and swap space found, skipping")

	elif swap == None:
		size = 4 - (mem)
		print(f"No swap found.\nCreating {size}GB swapfile")
		run(['fallocate', '-l', size+'G', '/swapfile'])
		run(['chmod', '600', '/swapfile'])
		run(['mkswap', '/swapfile'])
		run(['swapon', '/swapfile'])
		f = open('/etc/fstab', 'a')
		f.write("/swapfile\tnone\tswap\tsw\t0\t0")
		f.close
		print("\t========== Complete ==========\n\n")
      
	elif flocation == None and swap != None and mem+swap < 4:
		size = 4 - (mem+swap)
		print(f"Not enough free memory for Firod.\nCreating {size}GB swapfile")
		run(['fallocate', '-l', size+"G", '/swapfile'])
		run(['chmod', '600', '/swapfile'])
		run(['mkswap', '/swapfile'])
		run(['swapon', '/swapfile'])
		f = open('/etc/fstab', 'a')
		f.write("/swapfile\tnone\tswap\tsw\t0\t0")
		f.close
		print("\t========== Complete ==========\n\n")

### Change ownership of Firod and files to server user ###

def change_ownership():
	print("========== Changing Ownership of Firo required files ==========\n")
	run(['chown', uname+':'+uname, '/usr/local/bin/firod'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-qt'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-tx'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-cli'])
	run(['chown', '-R', uname+':'+uname, '/home/'+uname])
	print("\t========== Complete ==========\n\n")

### Delete downloaded files ###
def clean_up():
	print("========== Cleaning Up ==========\n")
	p = glob.glob(os.path.join(current_dir, 'firo-*'))
	for f in p:
		try:
			os.remove(f)
			print("Removed: "+f)
		except:
			shutil.rmtree(f)
			print("Removed: "+f)
	p = glob.glob(os.path.join(current_dir, 'SHA256SUMS*'))
	for f in p:
		os.remove(f)
		print("Removed: "+f)
	print("\t========== Complete ==========\n\n")

### Enable SSHD and FIROD ###
def enable_services():
	run(['systemctl', 'daemon-reload'])
	run(['systemctl', 'start', 'firod.service'])
	run(['systemctl', 'enable', 'firod.service'])
	try:
		run(['systemctl', 'restart', 'sshd.service'])
	except OSError as e:
		print(e)
		try:
			run(['systemctl', 'restart', 'ssh.service'])
		except OSError as e:
			print(e)
			print('Unable to restart sshd service, please do so manually.')
### Reboot System ###
	### using currently would cause user to be unable to check their ssh port making it harder for them to log in.
	### if ran with this enabled and you are having difficulty figuring out which port your sshd server has open 
	### run the command `nmap {local_ip}/{subnet}`
#def reboot():
#	run(['systemctl', 'reboot'])

### Run ###
			
def main():
	get_local_ip()
	static_ip()
	sshd_conf()
	deb_firewall_config()
	adduser()
	addkey()
	download_firod()
	checksum()
	extract_and_move()
	create_config()
	create_service()
	make_swap()
	change_ownership()
	clean_up()
	enable_services()
#	reboot()
main()
