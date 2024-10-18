from os import geteuid
#Check if superuser.

if geteuid() == 0:
	pass
else:
	print("")
	print('''
	   Please enter a valid privileged user password using the -sp flag, 
	   if the user is not `root` please enter a valid username using the -su flag: 
	   send_nodes -e "<server_public_ip_address>" -sp "<server_superuser_password>" -w "<wallet_encryption_password>"
	   ''')
	print("Exiting program...")
	exit()