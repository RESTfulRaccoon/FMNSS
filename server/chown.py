### Change ownership of Firod and files to server user ###
from subprocess import run
from variables import usr
print("========== Changing Ownership of Firo required files ==========\n")
run(['chown', usr+':'+usr, '/usr/local/bin/firod'])
run(['chown', usr+':'+usr, '/usr/local/bin/firo-qt'])
run(['chown', usr+':'+usr, '/usr/local/bin/firo-tx'])
run(['chown', usr+':'+usr, '/usr/local/bin/firo-cli'])
run(['chown', '-R', usr+':'+usr, '/home/'+usr])
print("\t========== Complete ==========\n\n")
