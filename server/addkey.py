def addkey(uname, key):
	if args.key == None:
		pass
	else:
		print(f"========== Adding ssh key to {uname} home directory ==========\n")
		f = open('/home/'+uname+'/.ssh/authorized_keys', 'w')
		f.write(key)
		f.close
		print("\t========== Complete ==========\n\n")