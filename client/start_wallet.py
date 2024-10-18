from subprocess import run
from variables import verbose

verbose("Starting `firod` on client computer")
try:
    run(['firod','-daemon'])
except OSError as e:
    ##make this silent unless verbose
    verbose(e)
### unlock wallet
## gather needed info from wallet
## lock wallet

znodeprivkey = "todo!"