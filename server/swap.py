### Ensure enough memory and virtual memory, add if needed ###
from subprocess import run
def swap():
	print("Checking if swap exists...")
	swap = run(['free'], capture_output=True)
	swap = str(swap.stdout).replace("b'", "").replace("\\n", " ").replace("\\t", " ").replace("'", "").split()
	pswap = run(['cat','/proc/swaps'], capture_output=True)
	pswap = str(pswap.stdout).replace("b'", "").replace("\\n", " ").replace("\\t", " ").replace("'", "").split()
	mem = swap[7]
	mem = round(int(mem)*.931323/1000000)

	if "file" in pswap:
		dex=pswap.index('file')
		flocation = pswap[dex+1]
	else:
		flocation = None
    
	if "Swap:" in swap:
		dex = swap.index("Swap:")
		swap = swap[dex+1]
		swap = round(int(swap)*.931323/1000000)
	else:
		swap = None

	if mem >= 4 and swap != None:
		print("Sufficent memory and swap space found, skipping")

	elif swap == None:
		size = 4 - (mem)
		print(f"No swap found.\nCreating {size}GB swapfile")
		run(['fallocate', '-l', size+'G', '/swapfile'])
		run(['chmod', '600', '/swapfile'])
		run(['mkswap', '/swapfile'])
		run(['swapon', '/swapfile'])
		f = open('/etc/fstab', 'a')
		f.write("/swapfile\tnone\tswap\tsw\t0\t0")
		f.close
		print("\t========== Complete ==========\n\n")
      
	elif flocation == None and swap != None and mem+swap < 4:
		size = 4 - (mem+swap)
		print(f"Not enough free memory for Firod.\nCreating {size}GB swapfile")
		run(['fallocate', '-l', size+"G", '/swapfile'])
		run(['chmod', '600', '/swapfile'])
		run(['mkswap', '/swapfile'])
		run(['swapon', '/swapfile'])
		f = open('/etc/fstab', 'a')
		f.write("/swapfile\tnone\tswap\tsw\t0\t0")
		f.close
		print("\t========== Complete ==========\n\n")
