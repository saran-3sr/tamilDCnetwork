import urllib.request
url='https://www.helloworld.org/'
response=urllib.request.urlopen(url)
webcontent=response.read().decode('UTF-8')
print(webcontent)
f1=open('./output.html','w')
f1.write(webcontent)
