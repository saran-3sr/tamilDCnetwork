import socket
def xor(a,b):
    result=[]
    for i in range(1,len(a)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
def moddiv(divent,divisor):
    pick=len(divisor)
    tmp=divent[0:pick]
    while pick<len(divent):
        if tmp[0]=='1':
            tmp=xor(divisor,tmp)+divent[pick]
        else:
            tmp=xor('0'*pick,tmp)+divent[pick]
        pick=pick+1
    if tmp[0]=='1':
        tmp=xor(divisor,tmp)
    else:
        tmp=xor('0'*pick,tmp)
    return tmp


def encode(word,key):
    len_k=len(key)
    appendedWord=word+'0'*(len_k-1)
    codeword=word+moddiv(appendedWord,key)
    return codeword
s=socket.socket()
Word=input("Enter the data word to send: ")
bitWord=(''.join(format(ord(x),'b')for x in Word))
print("Converted Bit word : ",bitWord )
key=input("Enter the keyword : ")
dataword=encode(bitWord,key)
print("Code word sent is -> ",dataword)