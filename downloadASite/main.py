import requests
url=input("Enter the URL to fetch : ")

try:
    r=requests.get(url,allow_redirects=True)
except:
    print("Error! Check the URL")
else:
    print(r.content)
    print(r.content.decode())
    # f=open('./Download.html',"w").write(content)
finally:
    print("Closing the program")

