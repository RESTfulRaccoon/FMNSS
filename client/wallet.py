import variables
from subprocess import run,CalledProcessError,PIPE
verbose = variables.verbose

print(__name__)
### START FIROD
verbose("Starting `firod` on client computer")
try:
    result = run(['firod','-daemon'], stdout=PIPE, stderr=PIPE)
    print('ERRORS: '+str(result.stdout))
except CalledProcessError as e:
    ##make this silent unless verbose
    verbose(e)

### UNLOCK CLIENT WALLET

### gather needed info from wallet

## LOCK CLIENT WALLET

znodeprivkey = "todo!"