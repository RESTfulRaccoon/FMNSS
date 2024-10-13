### Enable SSHD and FIROD ###
from subprocess import run
def enable_service():
	run(['systemctl', 'daemon-reload'])
	run(['systemctl', 'start', 'firod.service'])
	run(['systemctl', 'enable', 'firod.service'])
	try:
		run(['systemctl', 'restart', 'sshd.service'])
	except OSError as e:
		print(e)
		try:
			run(['systemctl', 'restart', 'ssh.service'])
		except OSError as e:
			print(e)
			print('Unable to restart sshd service, please do so manually.')