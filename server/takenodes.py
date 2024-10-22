###MAIN###
###MAKE THIS STANDALONE
### make a warning, if standalone == true...
## THIS CAN OVERWRITE IMPORTANT FILES THAT YOUR
## SYSTEM NEEDS TO RUN, IF YOU ARE NOT SURE WHAT YOU
## ARE DOING PLEASE DOWNLOAD THE CLIENT SCRIPT
## win command
## mac   ""
## linux ""
import argparse
parser = argparse.ArgumentParser(
	prog='takenodes',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	#usage='%(prog)s "server ip" "wallet password" "super user password"',
	description='''
is designed to work in conjunction with the Firo Client Side Start Script(sendnodes)\n
BE ADVISED:\n
Although this script can be used stand alone, it may break some current settings on your server.		
''',
	add_help=True,
	allow_abbrev=False,
)

parser.add_argument('usr', help="Firo Deamon user")
parser.add_argument('passwd', help="Root password")
parser.add_argument('port',help='SSH port to configure')
parser.add_argument('--no_firewall', action='store_true', help='Dont allow this script to configure your server firewall (default: %(default)s).')
parser.add_argument('--rpc_user', help="Firod RPC username")
parser.add_argument('--rpc_pass',help="Firod RPC password")
parser.add_argument('-v','--verbose', action='store_true')
args = parser.parse_args()

import test as test
import client.guid as guid

if __name__ == '__main__':
    test
    guid 
    print(__name__)