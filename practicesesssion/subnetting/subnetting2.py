ip=input("enter ip")
sub_mask=input("enter ")
#print("ip and submask is"ip+sub_mask)
sub_mask=int(sub_mask)
arr=ip.split(".")
print(arr)
binary=''
for i in arr:
    binary+=format(int(i),'08b')
print(binary)
index=32-sub_mask
list1=list(binary)
list2=list(binary)
for i in range(1,index+1):
    list1[-i]='0'
    list2[-i]='1'
print(list1)
print(list2)
temp1=''
temp2=''
for i in list1:
    temp1+=i
for i in list2:
    temp2+=i
print(temp1)
print(temp2)
bin1=[]
bin2=[]
for i in range(0,len(temp1),8):
    bin1.append(temp1[i:i+8])
    bin2.append(temp2[i:i+8])
print(bin1)
print(bin2)
ans1=''
ans2=''
for i in range(0,len(bin1)):
    bin1[i]=int(bin1[i],2)
    bin2[i]=int(bin2[i],2)
    ans1+=str(bin1[i])
    if(i!=3):
        ans1+='.'
    ans2+=str(bin2[i])
    if(i!=3):
        ans2+='.'
print(bin1)
print(bin2)
print(ans1)
print(ans2)