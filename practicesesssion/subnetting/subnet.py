import ipaddress

ip=input("Enter the ip address ")
mask=input("Enter the mask address ")
address=ip+'/'+mask
ip_address=ipaddress.ip_network(address,strict=False)
first,last=ip_address[0],ip_address[-1]
print(first,last)   