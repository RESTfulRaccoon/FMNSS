#!/usr/bin/env python3

#import input
from subprocess import run
##you already know this isnt going to work, fix it.
### Firewall configuration with IPTABLES ###
### UFW and IPTABLES conflict sometimes, to avoid the need of persistance just using IPTABLES

def deb_firewall_config(port, network, subnet, externalip, lan_addr):
	if args.no_firewall == False:
		print("========== Configuring IPTables... ==========\n")
		# Flush any previous rules
		run(['iptables', '-F'])
		# Whitelist
		run(['iptables', '-P', 'INPUT', 'DROP'])
		run(['iptables', '-P', 'FORWARD', 'DROP'])
		run(['iptables', '-P', 'OUTPUT', 'DROP'])
		# Ensure loopback traffic is configured
		run(['iptables', '-A', 'INPUT', '-i', 'lo', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-o', 'lo', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-s', '127.0.0.1/8', '-j', 'DROP'])
		# Default Deny and Allow:
		run(['iptables', '-A', 'OUTPUT', '-p', 'tcp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-p', 'udp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'OUTPUT', '-p', 'icmp', '-m', 'state', '--state', 'NEW,ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'udp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'icmp', '-m', 'state', '--state', 'ESTABLISHED', '-j', 'ACCEPT'])
		# Allow SSH and Masternode port
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-m', 'state', '--state', 'NEW', '-j', 'ACCEPT'])
		run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', '8168', '-m', 'state', '--state', 'NEW', '-j', 'ACCEPT'])
		run(['iptables', '-t', 'nat', '-A', 'OUTPUT','-s', network+'/'+subnet, '-d', externalip, '-j', 'DNAT', '--to-destination', lan_addr])
		# DROP all ip6 traffic
		run(['ip6tables', '-P', 'INPUT', 'DROP'])
		run(['ip6tables', '-P', 'OUTPUT', 'DROP'])
		run(['ip6tables', '-P', 'FORWARD', 'DROP'])
		run(['iptables-save'])
		print("\t========== Complete ==========\n\n")
