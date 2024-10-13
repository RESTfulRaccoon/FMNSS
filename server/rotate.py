### Create logrotate for Firod ###

def rotate(uname):
	f = open("/etc/logrotate.d/firo", "w")
	f.write("/home/"+uname+"/.firo/debug.log {\ndaily\nmissingok\nrotate 28\ncompress\ncopytruncate\n}")
	f.close
