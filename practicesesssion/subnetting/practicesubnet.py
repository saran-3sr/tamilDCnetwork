import ipaddress
ipaddr=input("Enter the IP address: ")
listIP=ipaddr.split('.')
mask=int(input("Enter the mask value:  "))
bin1=''
for i in listIP:
    bin1+=format(int(i),'08b')
print(bin1)
list1=list(bin1)
list2=list(bin1)
subNet=32-mask
for i in range(1,subNet+1):
    list1[-i]='0'
    list2[-i]='1'
print(list1)
print(list2)
temp1=''
temp2=''
for i in range(len(list1)):
    temp1+=list1[i]
    temp2+=list2[i]
print(temp1)
print(temp2)
bin1=[]
bin2=[]
for i in range(0,len(temp1),8):
    bin1.append(temp1[i:i+8])
    bin2.append(temp2[i:i+8])

ans1=''
ans2=''
for i in range(len(bin1)):
    bin1[i]=int(bin1[i],2)
    bin2[i]=int(bin2[i],2)
    ans1+=str(bin1[i])
    ans2+=str(bin2[i])
    if i!=3:
        ans1+='.'
        ans2+='.'
print(ans1)
print(ans2)