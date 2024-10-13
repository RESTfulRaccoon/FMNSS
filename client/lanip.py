import socket
from ipaddress import IPv4Network
from fcntl import ioctl
from struct import pack

def lanip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('1.1.1.1', 80))
	my_ip = s.getsockname()[0]
	s.close()
	iface = socket.if_nameindex()
	n = 0
	for n in range(len(iface)):
		i = iface[n][1]
		try: 
			subnetet_mask = socket.inet_ntoa(ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, pack(b'256s', i.encode()))[20:24])
		except OSError as error:
			print(error)
	my_network = IPv4Network(my_ip+'/'+subnetet_mask, strict=False)
	netmask = subnetet_mask
	network_if = i

	if lan_addr == "":
		lan_addr = str(my_ip)

	if subnet == "":
		subnet = str(my_network).split("/")[1]
	
	network = str(my_network).split("/")[0]
	broadcast = lan_addr[:lan_addr.rfind('.')+1] + '255'
	gateway = lan_addr[:lan_addr.rfind('.')+1] + '1'
	
	return network, broadcast, gateway, my_network, netmask, network_if
