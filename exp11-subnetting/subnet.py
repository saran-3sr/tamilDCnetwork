import ipaddress
ip= input("Enter the IP address")
# mask=input("Enter the mask address")
# result=ip+'/'+mask
bitpos=int(input("Enter the Bit position : "))
mask=str(32-bitpos)
result=ip+'/'+mask

print("Subnet Mask:",result)
addr=ipaddress.ip_network(result,strict=False)
first,last=addr[0],addr[-1]

print(first,last)