### Create Firod system daemon ###

def sysd(uname):
	f = open("/etc/systemd/system/firod.service", "w")
	f.write(
f'''
[Unit]
Description=Firo daemon
After=network.target

[Service]
Type=forking
Restart=always
RestartSec=30

User={uname}
Group={uname}
PIDFile=/home/{uname}/.firo/firod.pid

ExecStart=/usr/local/bin/firod
ExecStop=/usr/local/bin/firo-cli stop

[Install]
WantedBy=multi-user.target
'''
	)
	f.close
