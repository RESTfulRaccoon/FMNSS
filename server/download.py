from subprocess import run

def download(firo_core_version):
	charch = 0

	if arch == 'x86_64':
		charch = 1
	print("========== Downloading Firo Binaries tarball and Checksums... ==========\n")
	run(['wget', '-q', firo_core_version.json()['assets'][charch]['browser_download_url']])
	run(['wget', '-q', firo_core_version.json()['assets'][6]['browser_download_url']])
	print("\t========== Complete ==========\n\n")
