from subprocess import run, check_output


def version():
	arch = str(check_output('arch')).replace("b'","").replace("\\n'","").strip()
	try:
		firo_core_version = run(['curl','https://api.github.com/repos/firoorg/firo/releases/latest','|','jq','-r','.tagname'])
		print(firo_core_version)
	except OSError as e:
		print(e)
		exit()
	
	numb = 0
	if arch == 'x86_64':
		numb = 1
	else:
		print("This script is designed for Linux based systems on ARM or x86_64 architecture\nExiting...")
		exit()
	tarball = "".join(firo_core_version.json()["assets"][numb]["browser_download_url"].split("/")[-1])

	return tarball

version()