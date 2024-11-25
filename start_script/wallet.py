from subprocess import run,CalledProcessError,PIPE
from variables import verbose

### CHECK WALLET VERSION

### LOCAL FIROD
verbose("Starting `firod` on client computer")
try:
    result = run(['firod','-daemon'], stdout=PIPE, stderr=PIPE)
    print('ERRORS: '+str(result.stdout))
except CalledProcessError as e:
    ##make this silent unless verbose
    verbose(e)

### UNLOCK WALLET
### Check for wallet with 1000 balance && 1 tx
### Ensure not used by other node
### Lock unspent
### Owner address
### Payout address
### feesourceaddress (not an address == 1000 firo)
### operator keys
znodeprivkey = "todo!"
## LOCK WALLET

## Need to figure out why ssh-keygen -lf wont work through paramiko

# result = run(['ssh-keygen','-lf',key,'|','cut','--delimiter','" "','--fields=4'],stdout=PIPE)
# key_type=result
# if key_type != '(RSA)' or '(DSS)' or '(ED25519)' or '(EDCSA)':
#     try:
#         result = run(['ssh-keygen','-lf',key,'|','cut','--delimiter','" "','--fields=6'],stdout=PIPE)
#         key_type = result
#         if key_type != '(RSA)' or '(DSS)' or '(ED25519)' or '(EDCSA)':
#             print("error")
#             exit()
#     except OSError as e:
#                 print(e)
# if key_type == '(RSA)':
#     k = paramiko.RSAKey.from_private_key_file(key)
# elif key_type == '(DSS)':
#     k = paramiko.DSSKey.from_private_key_file(key)
# elif key_type == '(ED25519)':
#     k=paramiko.Ed25519Key.from_private_key_file(key)
# elif key_type == '(EDCSA)':
#     k=paramiko.ECDSAKey.from_private_key_file(key)



