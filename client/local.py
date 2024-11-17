from subprocess import run,CalledProcessError,PIPE
from variables import verbose, keyname, keypath,sshkeypass,suusr,ext
from local_fun import key_check
### LOCAL FIROD
verbose("Starting `firod` on client computer")
try:
    result = run(['firod','-daemon'], stdout=PIPE, stderr=PIPE)
    print('ERRORS: '+str(result.stdout))
except CalledProcessError as e:
    ##make this silent unless verbose
    verbose(e)

### CHECK WALLET VERSION

## UNLOCK CLIENT WALLET

## gather needed info from wallet

## LOCK CLIENT WALLET

znodeprivkey = "todo!"

### SSH KEY
gen_key=False
if keyname == None:
    keyname=key_check(keypath)
    fullkey=keypath+keyname
    gen_key= True
    try:
        result = run(['ssh-keygen','-t','ed25519','-f',fullkey,'-N',sshkeypass],stdout=PIPE,universal_newlines=True)
        verbose(result.stdout)
    except CalledProcessError as e:
        verbose(e)   
        run(['firo-cli','stop'])
        exit()
elif keyname != None:
    fullkey=keypath+keyname
    try:
        result = run(['ssh-keygen','-lf',fullkey,'|','cut','--delimiter','" "','--fields=4'],stdout=PIPE)
        key_type=result
        if key_type != '(RSA)' or '(DSS)' or '(ED25519)' or '(EDCSA)':
            try:
                result = run(['ssh-keygen','-lf',fullkey,'|','cut','--delimiter','" "','--fields=6'],stdout=PIPE)
                key_type = result
                if key_type != '(RSA)' or '(DSS)' or '(ED25519)' or '(EDCSA)':
                    print("error")
                    exit()
            except CalledProcessError as e:
                verbose(e)
    except:
        print(f"{fullkey} is not a valid SSH key.")
        run(['firo-cli','stop'])
        exit()
### COPY ID
try:
    run(['ssh-copy-id','-i',fullkey,suusr+':'+ext])
except CalledProcessError as e:
    print(e)
