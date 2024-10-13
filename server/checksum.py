### Validate intrgrity of tarball with CHECKSUMS ###
from shutil import rmtree
from subprocess import check_output

def checksum(arch, current_dir, tarball):
	vers = 'aarch64'

	if arch == 'x86_64':
		vers = 'linux64'

	print("========== Checking download integrity ==========\n")

	for lines in open('SHA256SUMS', 'r'):
		if vers in lines:
			line = lines
   
	check1 = str(check_output(['sha256sum', tarball])).replace("b'"," ").replace("\\n'","").strip()
	check2 = str(line).strip()
	if check1 == check2:
		print("========== \tIntegrity Verified... ==========\n")
	else:
		rmtree(current_dir+"/"+tarball)
		rmtree(current_dir+'/SHA256SUMS')