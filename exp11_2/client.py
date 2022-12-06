import urllib.request, urllib.error, urllib.parse

url = 'https://ysyouthgct.in/'

response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')
print(response)
f = open('ysc.html', 'w')
f.write(webContent)
print("Html file saved")
f.close()