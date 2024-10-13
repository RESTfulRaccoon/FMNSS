
import os
### Create Firod config file ###

def create_config(uname,rpc_username, rpc_passwd, externalip, znodeprivkey):
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
