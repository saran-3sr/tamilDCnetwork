import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
li=[] #get dataa
li3=[] #copy of original data
li1=[] #DSSS data
li4=[] #DSSS to original data
li2=[1,0,0,0,0,0,0,0,0,0,1] #Chip generated Sequence
li5=[] #Clock cycle
li6=[] #DSSS in voltage
li7=[] #Error DSSS in voltage
print("Direct Sequence Spread Spectrum using python and matplot.")
n=int(input("Enter the number of bits to transfer: "))
print("Enter the Data :")
flag=1
for i in range(0,n):
    li.append(int(input()))
li3=li.copy()
for i in li:
    if i==1:
        for j in range(0,11):
            li1.append(li2[j])    
            li5.append(flag)
            flag+=1
    else:
        for j in range(0,11):
            if li2[j]==0:
                li1.append(1)
                li5.append(flag)
                flag+=1
            else:
                li1.append(0)
                li5.append(flag)
                flag+=1            
for i in li1:
    if i==0:
        li6.append(-5)
    else:
        li6.append(5)                   
print("The DSSS pattern is:",li1)       
n2=int(input("Enter Error bit rate:"))
print("The original data:",li3)
count=0
for i in range(0,n,4):
    if(li[i])==0:
        li[i]=1
        count+=1
    else:
        li[i]=0
        count+=1
print("Errored data",li)        
for i in range(0,11*n,4):
    if(li1[i])==0:
        li1[i]=1
        count+=1
    else:
        li1[i]=0
print("Errored DSSS:",li1)        
for i in range(0,n):
    count2=0
    for j in range(11*i,11*i+11):
        if (li1[j]==1):
            count2+=1
    if(count2>5):
        li4.append(0)
    else:
        li4.append(1)        
print("The data from DSSS:",li4)        
count3=0
count4=0
for i in range(0,n):
    if li3[i]!=li[i]:
        count3+=1
    if li3[i]!=li4[i]:
        count4+=1    
for i in li1:
    if i==0:
        li7.append(-5)
    else:
        li7.append(5)            
print("Original Errored Bits",count3)
print("Error on data bits from Dsss",count4)
print("Error in Normal transmission is:",int(count3/n*100),"%")
print("Error in DSSS transmission is:",int(count4/n*100),"%")
plt.bar(li5,li6,align='edge')
plt.xlabel("Clock Cycle")
plt.ylabel("Voltage")
plt.title("DSSS")
plt.show()
plt2.bar(li5,li7,align='edge')
plt2.xlabel("Clock Cycle")
plt2.ylabel("Voltage")
plt2.title("Errored DSSS")
plt2.show()