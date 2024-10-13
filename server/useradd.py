from pwd import getpwall
from subprocess import run
from os import system
### Add user if user doesn't exist ###
	
def adduser(uname, password):
	print(f"========== Checking if {uname} exists as a user ==========\n")
	usernames = [x[0] for x in getpwall()]
	if uname in usernames:
		print(f"{uname} is already a user, skipping this step")
	else:	
		print(f"========== Adding {uname} user... ==========\n")
		run(['useradd', '-m', uname])
		usr = 'firo:'+password
		cmd = 'printf "'+usr+'" | chpasswd'
		system(cmd)
		print("\t========== Complete ==========\n\n")
