#!/usr/bin/env python3

import input

### Output File
## Client-Side

o = open(output, 'w')
o.write("This is your output file all of the information from this script will be gathered here\nSafe this information somewhere safe!!! Failure to do so might result in needing to completely remake your Masternode!!!\n\n\n")
o.close
o = open(output, 'a')
## INFORMATION TO BE GATHERED FROM checks.get_local_ip
## is all of this needed? could be helpful for "debugging" if script fails in some way..
o.write(
f'''
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx FIRO CONFIG xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

RPC Username: {rpc_username}
RPC Password: {rpc_passwd}
ZnodePrivKey: {znodeprivkey}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxx USER INFORMATION xxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Firo Daemon User: {uname}
Daemon User Password: {password}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxx NETWORK INFORMATION xxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Local IP Address: {lan_addr}/{subnet}
Local Network: {network}
Local Subnet: {netmask}
Gateway IP Address: {gateway}
Broadcast IP Address: {broadcast}
External IP Address: {externalip}
SSH Port: {port}

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxx ERRORS xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
'''
)
o.close