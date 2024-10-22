#!/usr/bin/env python3

import os
import variables
### Sshd configuration ###
## Server Side

def sshd_conf(port):
	print("========== Configuring SSHD... ==========\n")
	f = open('/etc/ssh/sshd_config', 'a')
	f.write('PermitRootLogin no\nMaxAuthTries 3\nMaxSessions 3\n')
	if variables.pubkey == None:
		pass
	else:
		f.write('PasswordAuthentication no\n')
	if port == '22':
		pass
	else:
		f.write('Port '+port+'\n')
	f.close
	## This is clever but i should just disable cloud-init
	if os.path.exists("/etc/ssh/sshd_config.d/50-cloud-init.conf"):
		os.remove('/etc/ssh/sshd_config.d/50-cloud-init.conf')
	## Double check more of these crazy files dont exist
	if os.path.exists("/etc/sysconfig/sshd-permitrootlogin"):
		os.remove("/etc/sysconfig/sshd-permitrootlogin")
	print("\t========== Complete ==========\n\n")
