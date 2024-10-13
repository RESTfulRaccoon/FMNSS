#!/usr/bin/env python3

### Argument Parser ###
import argparse
import textwrap

def argparse():
	parser = argparse.ArgumentParser(
		prog='firo_ssmnss',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		usage='%(prog)s <server_public_ip_address> <server_username> <server_superuser_password>',
		description=textwrap.dedent('''
		todo
        	todo
            	todo
                	todo
		'''),
		add_help=True,
		allow_abbrev=False,
		)

	parser.add_argument('-k', '--key', metavar='string format of public ssh key', help='Public key you would like to use for Secure Shell connections.')
	parser.add_argument('-u', '--username', metavar='raccFoon', default='firo', help='Name of Firo Daemon user (default: %(default)s).')
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
	args = parser.parse_args()
	return args