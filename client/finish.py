from variables import nofinish,clean_up, verbose
from subprocess import run

### REMOVE CACHE
run(clean_up)
verbose("Clearing cache...")
if nofinish == True:
    print(__name__)
else:
### Cronjob to finsish the setup after server node is synced
## can you have the client ping the server rpc for some info? this would be best route
# ping > if true run scripte else wait X time
    print("TODO: "+__name__)