import argparse

parser = argparse.ArgumentParser(
	prog='sendnodes',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	usage='%(prog)s "server ip" "super user password" "wallet password"',
	description='''
		todo
		todo
		todo
		''',
	add_help=True,
	allow_abbrev=False,
)

parser.add_argument('server_ip', help='External IP address of server where node will be hosted.',type=str)
## change this to just passwd
parser.add_argument('superuser_pass', help='Password of root or server superuser', type=str)
parser.add_argument('wallet_password', help='''
			Your wallets encryption password.
			This is needed to generate your BLSPrivKey and register your node.
			It is required to have your wallet encrypted to run this script!!!.
					''',type=str)
parser.add_argument('--superuser', metavar='raccoon', default='root', help='Name of Privlaged server user (default: %(default)s).')
parser.add_argument('-u','--usr', metavar='firo', help='Name of firo daemon user external server (default: firo).',type=str)
parser.add_argument('-p','-passwd',help="Password of non-privladged firo daemon user.")
parser.add_argument('-P','--port', help='The port you would like ssh to use while connecting.')
parser.add_argument('--ssh-key-name',help='Public key you would like to use for Secure Shell connections.(default: ed25519_firo_0)')
parser.add_argument('--rpc-user', help='Enter username for firo rpc. (default: will be 10 randomly generated letters.)')
parser.add_argument('--rpc-pass',help='Enter password for firo rpc. (default: will be randomly generated.)')
parser.add_argument('--sshkeypass', help='create a password for your ssh key, this is recommended but not required' )
parser.add_argument('--no-firewall', action='store_true', help='Dont allow this script to configure your server firewall (default: %(default)s).')
parser.add_argument('--keep-port', action='store_true', help='Use this if you would like to keep your ssh port as 22 (default: %(default)s)')
parser.add_argument('-v','--verbose', action='store_true', help='Make script more verbose')
args = parser.parse_args()

import wallet
import server
import finish

print(__name__)
if __name__ == "__main__":
    wallet
    server
    finish