### Change ownership of Firod and files to server user ###
from subprocess import run
def change_ownership(uname):
	print("========== Changing Ownership of Firo required files ==========\n")
	run(['chown', uname+':'+uname, '/usr/local/bin/firod'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-qt'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-tx'])
	run(['chown', uname+':'+uname, '/usr/local/bin/firo-cli'])
	run(['chown', '-R', uname+':'+uname, '/home/'+uname])
	print("\t========== Complete ==========\n\n")
