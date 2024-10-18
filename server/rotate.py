### Create logrotate for Firod ###
from variables import usr
def rotate(usr):
	f = open("/etc/logrotate.d/firo", "w")
	f.write("/home/"+usr+"/.firo/debug.log {\ndaily\nmissingok\nrotate 28\ncompress\ncopytruncate\n}")
	f.close
