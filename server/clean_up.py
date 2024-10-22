import glob
import os
from shutil import rmtree
### Delete downloaded files ###
def clean_up(current_dir):
	print("========== Cleaning Up ==========\n")
	p = glob.glob(os.path.join(current_dir, 'firo-*'))
	for f in p:
		try:
			os.remove(f)
			print("Removed: "+f)
		except:
			rmtree(f)
			print("Removed: "+f)
	p = glob.glob(os.path.join(current_dir, 'SHA256SUMS*'))
	for f in p:
		os.remove(f)
		print("Removed: "+f)
	print("\t========== Complete ==========\n\n")

### REMOVE CACHE