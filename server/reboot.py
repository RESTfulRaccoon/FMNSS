from subprocess import run
### Reboot System ###
	### using currently would cause user to be unable to check their ssh port making it harder for them to log in.
	### if ran with this enabled and you are having difficulty figuring out which port your sshd server has open 
	### run the command `nmap {local_ip}/{subnet}`
def reboot():
	run(['systemctl', 'reboot'])