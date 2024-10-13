from os import geteuid

#Check if superuser.
def guid():
	if geteuid() == 0:
		pass
	else:
		print("You must be a privileged user to run this program!")
		print("Please enter your servers password: {example}")
		print("Exiting program...")
		exit()