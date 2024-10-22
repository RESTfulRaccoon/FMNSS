from variables import verbose,keypath,keyname,sshkeypass,suusr,ext
from local_fun import key_check
from subprocess import run, CalledProcessError, PIPE

### GEN KEY
## If `--ssh_key_name` not selected ganerate one
if keyname == None:
    keyname=key_check(keypath)
    fullkey=keypath+keyname
    try:
        result = run(['ssh-keygen','-t','ed25519','-f',fullkey,'-N',sshkeypass],stdout=PIPE,universal_newlines=True)
        verbose(result.stdout)
    except CalledProcessError as e:
        verbose(e)
elif keyname != None:
    if keyname[-4:] == '.pub':
        fullkey=keypath+keyname[:-4]
    else:
        keyname=keyname
        fullkey = keypath+keyname
    result = run(['ssh-keygen','-l','-f',fullkey+'.pub'], stderr=PIPE)
    if result.stderr:
        print(str(result.stderr).replace("b'", "").replace("\\r\\n", ""))    
        keyname=key_check(keypath)
        print("Public key did not work...\nAutomatically creating an ssh key: "+keyname)
        fullkey=keypath+keyname
        try:
            result = run(['ssh-keygen','-t','ed25519','-f',fullkey,'-N',sshkeypass],stdout=PIPE,universal_newlines=True)
            print(result.stdout)
        except CalledProcessError as e:
            verbose(e)

### COPY ID
try:
    result = run(['ssh-copy-id','-i',fullkey,suusr+':'+ext],stdout=PIPE, stderr=PIPE,universal_newlines=True)
    if result.stderr:
        run(['rm',fullkey, fullkey+'.pub'])
        print("ERROR:")
        verbose(result.stderr)
        print("removing created keyfiles")
        print("exiting...")
        #exit()
except CalledProcessError as e:
    run(['rm',fullkey, fullkey+'.pub'])
    print(e)
    print("removing created keyfiles")
    print("exiting...")
    #exit()

### SSH into the server
print("TODO: SSH IN")
### Check if you are root if this fails remove the key too
print('TODO:uid')
### Make sure the server is up to date and depends for script are installed.
print("TODO: DOWNLOAD DEPENDS && UPDATE IF NEEDED,")
### download takenodes.py
print("TODO: download takenodes.py")
### Run takenodes.py {ALL INPUT REQUIRED}

print(__name__)