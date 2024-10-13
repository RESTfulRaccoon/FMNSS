### Extract tarball and move binaries to /usr/local/bin ###
import tarfile
import glob
from shutil import copy

def extract_mv(tarball, current_dir,op_file,uname):
	print("========== Extracting Firo Binaries ==========\n")
	tar = tarfile.open(tarball.strip(), "r:gz")
	tar.extractall()
	tar.close
	print("\t========== Complete ==========\n\n")
	print('========== Moving binaries to /usr/local/bin ==========')
	for p in glob.glob(current_dir+'/firo-*/bin/firo*'):
		copy(p, "/usr/local/bin/")
		print("Moved "+p+" to /usr/loca/bin/")
	print("\t========== Complete ==========\n\n")
	copy(op_file, '/home/'+uname+'/')
