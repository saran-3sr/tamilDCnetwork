import socket
def xor(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(code,key):
    
    pick=len(key)
    tmp=code[0:pick]
    while pick<len(code):
        if tmp[0]=='1':
            tmp=xor(key,tmp)+code[pick]
        else:
            tmp=xor('0'*pick,tmp)+code[pick]
        pick=pick+1
    
    if tmp[0]=='1':
        tmp=xor(key,tmp)
    else:
        tmp=xor('0'*pick,tmp)
    word=tmp
    return word

def encode(received,key):
    len_k=len(key)
    receivedApend=received+'0'*(len_k-1)
    # print(receivedApend)
    print(mod2div(receivedApend,key))
    return mod2div(receivedApend,key)

ReceivedWord=input("Enter the Received Code : ")
key=input("Enter the Key value : ") 
remainder=encode(ReceivedWord,key)
check='0'*(len(key)-1)
if remainder==check:
    print("No error")
else:
    print("Error")